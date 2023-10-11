# SerialFormatter (Microserve)

## Overview

This small application is used to parse a comma or new-line separated list of serial number strings and create a new string where each parsed element is comma separated, enclosed in single quotes, and placed inside of brackets. Its main use is to speed up the process of searching for defective serial numbers in the database after copying them from ConnectWise while working at Microserve. When creating SQL transactions using the "IN" keyword string literals must be enclosed in quotations and placed inside of brackets, this application avoids the user having to manually add the quotes to each string.

## Use

Serials copied from ConnectWise are: 456456,457667,6577675,45433,565432 \
paste the entire string into the textbox, select the quotations checkbox, set the type of brackets and then click format.

For instance if we had seleceted "()" brackets, then the resulting formatted string would be:
### &ensp;&ensp;&ensp;&ensp;('456456','457667','6577675','45433','565432')
