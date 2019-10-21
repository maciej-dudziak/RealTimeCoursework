#include <MKW41Z4.h>
#include <Board_LED.h>
#include <FreeRTOS.h>
#include <Task.h>
#include <queue.h>

static void prvQueueReceiveTask (void *pvParameters); //Forward references
static void prvQueueSendTask		(void *pvParameters);
static xQueueHandle xQueue = NULL;	// The queue used by both tasks, xQueueHandle is a pointer to the QueueDefinition struct, defined on queue.c

int main(void)	{
	//Free RTOS heap structures
	#define HEAP_SIZE 0x10000
	static uint8_t FreeRTOS_heap[HEAP_SIZE];
	const HeapRegion_t xHeapRegions[] = 
		{
				{ FreeRTOS_heap, HEAP_SIZE },
				{NULL, 0}
		};
		SystemInit();
		SystemCoreClockUpdate();
		
		LED_Initialize();
		vPortDefineHeapRegions (xHeapRegions);
		xQueue = xQueueCreate (1, sizeof( unsigned long) );
		if (xQueue !=NULL) {
			xTaskCreate( prvQueueReceiveTask, "Rx",
									configMINIMAL_STACK_SIZE, NULL, tskIDLE_PRIORITY + 2, NULL);
			xTaskCreate( prvQueueSendTask,	"Tx",
									configMINIMAL_STACK_SIZE, NULL, tskIDLE_PRIORITY + 1, NULL);
			vTaskStartScheduler();
		}
		LED_On(0);
		while(1);
}

static void prvQueueSendTask( void *pvParameters ) {
	portTickType xNextWakeTime;
	const unsigned long ulValueToSend = 100UL;
	xNextWakeTime = xTaskGetTickCount();
	while(1) {
		vTaskDelayUntil( &xNextWakeTime, 500 / portTICK_PERIOD_MS );
		xQueueSend( xQueue, &ulValueToSend, 0 ); } }

static void prvQueueReceiveTask( void *pvParameters) {
	int LED_is_on = 0;
	unsigned long ulReceivedValue;
	while(1) {
		xQueueReceive( xQueue, &ulReceivedValue, portMAX_DELAY );
		if ( ulReceivedValue == 100UL ) {
			LED_is_on = !LED_is_on; LED_is_on ? LED_On(2):LED_Off(2); } } }