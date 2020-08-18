#include <stdio.h>
#include "pb/pb_encode.h"
#include "pb/pb_decode.h"
#include "simplestm32.pb.h"
#include <stdint.h>




int main()
{
    uint8_t tx_buffer[20],rx_buffer[20],n;
   
    
    comMessage msg_tx=comMessage_init_zero;
    pb_ostream_t tx_stream=pb_ostream_from_buffer(tx_buffer,sizeof(tx_buffer));
    msg_tx.pot_val1=45;
    msg_tx.pot_val2=48;
    pb_encode(&tx_stream,comMessage_fields,&msg_tx);
    printf("%d byte is serialized\n",tx_stream.bytes_written);

    strncpy(rx_buffer,tx_buffer,tx_stream.bytes_written);

    comMessage msg_rx=comMessage_init_zero;
    pb_istream_t rx_stream=pb_istream_from_buffer(rx_buffer,sizeof(rx_buffer));
    pb_decode(&rx_stream,comMessage_fields,&msg_rx);
    printf("pot_val1 : %d \npot_val2 : %d \n",msg_rx.pot_val1,msg_rx.pot_val2);    



    

    return 0;
}