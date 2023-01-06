"This file contains a sample of solutions that your code should return"

STOCKS_TO_TEST = ['AVGO', 'TMUS', 'QCOM', 'ROST', 'ISRG', 'ORLY', 'SBUX', 'MU',
       'LRCX', 'CMCSA', 'GOOGL', 'ATVI', 'COST', 'CSCO', 'NVDA', 'AMZN',
       'PYPL', 'TXN', 'INTC', 'GILD', 'AAPL', 'CTSH', 'VRTX', 'REGN',
       'ADI', 'FISV', 'BIIB', 'KHC', 'MSFT', 'AMD', 'INTU', 'AMAT',
       'CHTR', 'FB', 'ILMN', 'PEP', 'MDLZ', 'NFLX', 'AMGN', 'ADBE', 'WBA',
       'EBAY', 'ADP', 'CSX', 'MAR', 'BKNG', 'TSLA', 'XEL', 'NXPI']

STATS_SOLUTION = {
    "AAPL" : [173, 239, 327],
    "TSLA" : [179, 353.72, 917],
    "FB" : [146, 190.77, 223]
}

TIME_SERIES_SOLUTION = {
    "AAPL" : [[365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730],
              [191.0, 194.0, 195.0, 196.0, 197.0, 200.0, 200.0, 200.0, 200.0, 201.0, 199.0, 199.0, 199.0, 199.0, 199.0, 199.0, 203.0, 204.0, 205.0, 205.0, 205.0, 205.0, 207.0, 207.0, 205.0, 204.0, 205.0, 205.0, 205.0, 201.0, 211.0, 209.0, 212.0, 208.0, 208.0, 208.0, 203.0, 203.0, 201.0, 197.0, 186.0, 186.0, 186.0, 189.0, 191.0, 190.0, 189.0, 183.0, 183.0, 183.0, 187.0, 183.0, 180.0, 179.0, 178.0, 178.0, 178.0, 178.0, 177.0, 178.0, 175.0, 173.0, 173.0, 173.0, 180.0, 183.0, 185.0, 190.0, 193.0, 193.0, 193.0, 195.0, 194.0, 194.0, 193.0, 194.0, 194.0, 194.0, 198.0, 198.0, 199.0, 199.0, 199.0, 199.0, 199.0, 196.0, 200.0, 200.0, 198.0, 202.0, 202.0, 202.0, 203.0, 204.0, 204.0, 204.0, 200.0, 200.0, 200.0, 201.0, 203.0, 202.0, 203.0, 205.0, 205.0, 205.0, 204.0, 203.0, 206.0, 203.0, 207.0, 207.0, 207.0, 209.0, 209.0, 207.0, 208.0, 210.0, 210.0, 210.0, 209.0, 213.0, 208.0, 204.0, 193.0, 193.0, 193.0, 197.0, 199.0, 203.0, 201.0, 200.0, 200.0, 200.0, 209.0, 203.0, 202.0, 206.0, 210.0, 210.0, 210.0, 210.0, 213.0, 212.0, 203.0, 206.0, 206.0, 206.0, 204.0, 206.0, 209.0, 209.0, 206.0, 206.0, 206.0, 206.0, 209.0, 213.0, 213.0, 214.0, 214.0, 214.0, 217.0, 224.0, 223.0, 219.0, 220.0, 220.0, 220.0, 221.0, 223.0, 221.0, 218.0, 219.0, 219.0, 219.0, 218.0, 221.0, 220.0, 219.0, 224.0, 224.0, 224.0, 225.0, 219.0, 221.0, 227.0, 227.0, 227.0, 227.0, 224.0, 227.0, 230.0, 236.0, 236.0, 236.0, 236.0, 235.0, 234.0, 235.0, 236.0, 241.0, 241.0, 241.0, 240.0, 243.0, 244.0, 247.0, 249.0, 249.0, 249.0, 243.0, 243.0, 249.0, 256.0, 258.0, 258.0, 258.0, 257.0, 257.0, 259.0, 260.0, 262.0, 262.0, 262.0, 262.0, 264.0, 263.0, 266.0, 267.0, 267.0, 267.0, 266.0, 263.0, 262.0, 262.0, 266.0, 266.0, 266.0, 264.0, 268.0, 267.0, 267.0, 264.0, 264.0, 264.0, 259.0, 262.0, 266.0, 271.0, 267.0, 267.0, 267.0, 268.0, 271.0, 271.0, 275.0, 280.0, 280.0, 280.0, 280.0, 280.0, 280.0, 279.0, 284.0, 284.0, 284.0, 284.0, 290.0, 290.0, 290.0, 292.0, 292.0, 292.0, 294.0, 300.0, 300.0, 297.0, 300.0, 300.0, 300.0, 298.0, 303.0, 310.0, 310.0, 317.0, 317.0, 317.0, 313.0, 311.0, 315.0, 319.0, 317.0, 317.0, 317.0, 317.0, 318.0, 319.0, 318.0, 309.0, 309.0, 309.0, 318.0, 324.0, 324.0, 310.0, 309.0, 309.0, 309.0, 319.0, 321.0, 325.0, 320.0, 322.0, 322.0, 322.0, 320.0, 327.0, 325.0, 325.0, 319.0, 319.0, 319.0, 319.0, 324.0, 320.0, 313.0, 298.0, 298.0, 298.0, 288.0, 293.0, 274.0, 273.0, 299.0, 299.0, 299.0, 289.0, 303.0, 293.0, 289.0, 266.0, 266.0, 266.0, 285.0, 275.0, 248.0, 278.0, 242.0, 242.0, 242.0, 253.0, 247.0, 245.0, 229.0, 224.0, 224.0, 224.0, 247.0, 246.0, 258.0, 248.0, 255.0, 255.0, 255.0, 254.0]],
    "TSLA" : [[365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730],
                [289.0, 286.0, 292.0, 268.0, 275.0, 273.0, 273.0, 273.0, 272.0, 276.0, 268.0, 268.0, 266.0, 266.0, 266.0, 273.0, 271.0, 273.0, 263.0, 263.0, 263.0, 263.0, 264.0, 259.0, 248.0, 235.0, 241.0, 241.0, 241.0, 239.0, 234.0, 244.0, 255.0, 255.0, 255.0, 255.0, 247.0, 245.0, 242.0, 240.0, 227.0, 227.0, 227.0, 232.0, 232.0, 228.0, 211.0, 205.0, 205.0, 205.0, 205.0, 193.0, 195.0, 191.0, 189.0, 189.0, 189.0, 189.0, 190.0, 188.0, 185.0, 179.0, 179.0, 179.0, 194.0, 197.0, 206.0, 204.0, 213.0, 213.0, 213.0, 217.0, 209.0, 214.0, 215.0, 225.0, 225.0, 225.0, 225.0, 226.0, 220.0, 222.0, 224.0, 224.0, 224.0, 220.0, 219.0, 223.0, 223.0, 227.0, 227.0, 227.0, 225.0, 235.0, 233.0, 233.0, 230.0, 230.0, 230.0, 230.0, 239.0, 239.0, 245.0, 254.0, 254.0, 254.0, 252.0, 255.0, 254.0, 258.0, 256.0, 256.0, 256.0, 260.0, 265.0, 229.0, 228.0, 236.0, 236.0, 236.0, 242.0, 242.0, 234.0, 234.0, 228.0, 228.0, 228.0, 231.0, 233.0, 238.0, 235.0, 229.0, 229.0, 229.0, 235.0, 220.0, 216.0, 220.0, 227.0, 227.0, 227.0, 226.0, 221.0, 222.0, 211.0, 215.0, 215.0, 215.0, 214.0, 216.0, 222.0, 226.0, 225.0, 225.0, 225.0, 225.0, 221.0, 230.0, 227.0, 232.0, 232.0, 232.0, 236.0, 247.0, 246.0, 245.0, 243.0, 243.0, 243.0, 245.0, 243.0, 247.0, 241.0, 241.0, 241.0, 241.0, 223.0, 229.0, 243.0, 242.0, 241.0, 241.0, 241.0, 245.0, 243.0, 233.0, 231.0, 238.0, 238.0, 238.0, 240.0, 245.0, 245.0, 248.0, 257.0, 257.0, 257.0, 258.0, 260.0, 262.0, 257.0, 254.0, 254.0, 254.0, 256.0, 255.0, 300.0, 328.0, 328.0, 328.0, 328.0, 316.0, 315.0, 315.0, 313.0, 317.0, 317.0, 317.0, 317.0, 327.0, 336.0, 337.0, 345.0, 345.0, 345.0, 350.0, 346.0, 349.0, 352.0, 350.0, 350.0, 350.0, 360.0, 352.0, 355.0, 333.0, 336.0, 336.0, 336.0, 329.0, 331.0, 330.0, 330.0, 335.0, 335.0, 335.0, 336.0, 333.0, 330.0, 336.0, 340.0, 340.0, 340.0, 349.0, 353.0, 360.0, 358.0, 382.0, 382.0, 382.0, 379.0, 393.0, 404.0, 406.0, 419.0, 419.0, 419.0, 425.0, 431.0, 431.0, 430.0, 415.0, 415.0, 415.0, 418.0, 430.0, 430.0, 443.0, 452.0, 452.0, 452.0, 469.0, 492.0, 481.0, 478.0, 525.0, 525.0, 525.0, 538.0, 518.0, 513.0, 510.0, 547.0, 547.0, 547.0, 547.0, 570.0, 572.0, 565.0, 558.0, 558.0, 558.0, 567.0, 581.0, 641.0, 651.0, 780.0, 780.0, 780.0, 887.0, 735.0, 749.0, 748.0, 771.0, 771.0, 771.0, 774.0, 767.0, 804.0, 800.0, 858.0, 858.0, 858.0, 858.0, 917.0, 899.0, 901.0, 834.0, 834.0, 834.0, 800.0, 779.0, 679.0, 668.0, 744.0, 744.0, 744.0, 746.0, 750.0, 725.0, 703.0, 608.0, 608.0, 608.0, 645.0, 634.0, 561.0, 547.0, 445.0, 445.0, 445.0, 430.0, 361.0, 428.0, 428.0, 434.0, 434.0, 434.0, 505.0, 539.0, 528.0, 514.0, 502.0, 502.0, 502.0, 524.0]],
    "FB" : [[365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727, 728, 729, 730],
            [169.0, 174.0, 174.0, 176.0, 176.0, 175.0, 175.0, 175.0, 178.0, 178.0, 178.0, 179.0, 180.0, 180.0, 180.0, 179.0, 179.0, 178.0, 181.0, 181.0, 181.0, 181.0, 184.0, 183.0, 193.0, 191.0, 195.0, 195.0, 195.0, 193.0, 193.0, 193.0, 195.0, 194.0, 194.0, 194.0, 190.0, 190.0, 189.0, 188.0, 182.0, 182.0, 182.0, 181.0, 186.0, 187.0, 185.0, 183.0, 183.0, 183.0, 185.0, 185.0, 181.0, 181.0, 184.0, 184.0, 184.0, 184.0, 182.0, 183.0, 177.0, 164.0, 164.0, 164.0, 168.0, 168.0, 168.0, 173.0, 175.0, 175.0, 175.0, 178.0, 175.0, 177.0, 181.0, 189.0, 189.0, 189.0, 188.0, 187.0, 190.0, 191.0, 193.0, 193.0, 193.0, 189.0, 188.0, 190.0, 193.0, 193.0, 193.0, 193.0, 195.0, 197.0, 196.0, 196.0, 196.0, 196.0, 196.0, 199.0, 203.0, 201.0, 205.0, 204.0, 204.0, 204.0, 204.0, 202.0, 201.0, 198.0, 202.0, 202.0, 202.0, 202.0, 205.0, 201.0, 200.0, 196.0, 196.0, 196.0, 197.0, 194.0, 193.0, 189.0, 182.0, 182.0, 182.0, 185.0, 185.0, 190.0, 188.0, 185.0, 185.0, 185.0, 188.0, 180.0, 183.0, 184.0, 186.0, 186.0, 186.0, 184.0, 184.0, 182.0, 178.0, 180.0, 180.0, 180.0, 181.0, 182.0, 186.0, 186.0, 182.0, 182.0, 182.0, 182.0, 187.0, 191.0, 187.0, 189.0, 189.0, 189.0, 186.0, 188.0, 187.0, 187.0, 186.0, 186.0, 186.0, 188.0, 188.0, 190.0, 190.0, 187.0, 187.0, 187.0, 181.0, 183.0, 180.0, 177.0, 178.0, 178.0, 178.0, 176.0, 175.0, 179.0, 180.0, 180.0, 180.0, 180.0, 178.0, 180.0, 180.0, 184.0, 183.0, 183.0, 183.0, 189.0, 190.0, 190.0, 186.0, 190.0, 190.0, 190.0, 182.0, 186.0, 186.0, 188.0, 189.0, 189.0, 189.0, 189.0, 188.0, 192.0, 194.0, 195.0, 195.0, 195.0, 194.0, 192.0, 190.0, 191.0, 190.0, 190.0, 190.0, 194.0, 193.0, 193.0, 195.0, 197.0, 197.0, 197.0, 199.0, 198.0, 198.0, 199.0, 200.0, 200.0, 200.0, 199.0, 202.0, 202.0, 202.0, 200.0, 200.0, 200.0, 199.0, 199.0, 199.0, 201.0, 201.0, 201.0, 201.0, 201.0, 202.0, 197.0, 194.0, 198.0, 198.0, 198.0, 198.0, 202.0, 206.0, 206.0, 206.0, 206.0, 206.0, 205.0, 208.0, 208.0, 208.0, 204.0, 204.0, 204.0, 205.0, 210.0, 210.0, 209.0, 213.0, 213.0, 213.0, 213.0, 215.0, 218.0, 218.0, 222.0, 222.0, 222.0, 219.0, 221.0, 222.0, 222.0, 221.0, 221.0, 221.0, 221.0, 221.0, 220.0, 218.0, 215.0, 215.0, 215.0, 218.0, 223.0, 210.0, 202.0, 204.0, 204.0, 204.0, 210.0, 210.0, 211.0, 212.0, 213.0, 213.0, 213.0, 207.0, 211.0, 213.0, 214.0, 218.0, 218.0, 218.0, 218.0, 217.0, 215.0, 210.0, 201.0, 201.0, 201.0, 197.0, 197.0, 190.0, 192.0, 196.0, 196.0, 196.0, 186.0, 192.0, 185.0, 181.0, 170.0, 170.0, 170.0, 178.0, 170.0, 154.0, 170.0, 146.0, 146.0, 146.0, 149.0, 147.0, 153.0, 150.0, 148.0, 148.0, 148.0, 161.0, 156.0, 163.0, 157.0, 166.0, 166.0, 166.0, 167.0]]
}


SMALL_FULL_SOLUTION = {
    (0.04, "GOOGL", 1) : ['FB', 'INTC', 'MDLZ', 'MU', 'PEP'],
    (0.04, "GOOGL", 4) : ['AMZN', 'FISV', 'XEL'],
    (0.04) : 9,
    (0.04, "AAPL", 1) : ['BIIB', 'LRCX', 'MSFT'],
    (0.04, "AAPL", 2) : ['CHTR', 'VRTX'],
    (0.04, "AAPL", 4) : [],
    (0.08, "AAPL", 2) : ['REGN', 'TMUS'],
    (0.08) : 5,
}

MEDIUM_FULL_SOLUTION = {
    (0.06, "AAPL", 2) : ['ATVI', 'CHTR', 'ORA', 'ROKU'],
    (0.06) : 10,
    (0.1, "TSLA", 5) : ['NVDA'],
    (0.1) : 7,
}

LARGE_FULL_SOLUTION = {
    (0.05, "PEP", 5) : ['ABG', 'AC', 'ACV', 'ADAP', 'ADMA', 'ADRO', 'AES', 'AFINP', 'AGM', 'AGN', 'AGNCM', 'AGTC', 'AIT', 'AJRD', 'ALE', 'ALEC', 'ALNY', 'AMK', 'AMN', 'AMP', 'ARL', 'ARMP', 'ASRV', 'ATRI', 'AVGO', 'AWF', 'AWRE', 'AXP', 'BANX', 'BDJ', 'BFYT', 'BGS', 'BHE', 'BKE', 'BKNG', 'BMTC', 'BMY', 'BNS', 'BOX', 'BRO', 'BSA', 'BXMX', 'BYSI', 'CAF', 'CAJ', 'CASS', 'CBRE', 'CCNE', 'CDE', 'CDXC', 'CEE', 'CEL', 'CETV', 'CFFI', 'CGO', 'CHH', 'CHRW', 'CHW', 'CLAR', 'CNCE', 'CNFRL', 'CNO', 'COKE', 'CORE', 'COWNL', 'COWNZ', 'CPB', 'CPT', 'CRSP', 'CSBR', 'CSGP', 'CSX', 'CTBI', 'CTL', 'CTO', 'CUTR', 'CUZ', 'CVCO', 'CVR', 'CYH', 'CZNC', 'CZR', 'DCI', 'DCOM', 'DCOMP', 'DEAC', 'DEI', 'DEO', 'DGBP', 'DJP', 'DMAC', 'DOC', 'DRNA', 'DSSI', 'DTYL', 'EAD', 'EDU', 'EEA', 'EFL', 'ELAT', 'EMCF', 'ENS', 'ENTG', 'EPSN', 'ERII', 'ETB', 'ETG', 'ETNB', 'ETO', 'EV', 'EVT', 'EXC', 'EXFO', 'EXG', 'FANH', 'FATE', 'FAX', 'FBIOP', 'FBIZ', 'FENC', 'FFG', 'FIV', 'FIZZ', 'FLIC', 'FND', 'FRA', 'FRAF', 'FTNT', 'FVCB', 'FWONA', 'FWP', 'FWRD', 'FXNC', 'GCBC', 'GD', 'GDDY', 'GEF', 'GGM', 'GGN', 'GIB', 'GLU', 'GNK', 'GNW', 'GOF', 'GOODM', 'GORO', 'GSBC', 'GTY', 'HAPP', 'HASI', 'HEI', 'HIW', 'HPS', 'HVBC', 'HWBK', 'HYB', 'IAE', 'IBA', 'IBM', 'IDN', 'IFF', 'IFFT', 'IFS', 'III', 'IMUX', 'IMXI', 'INDB', 'IPG', 'IRTC', 'ITI', 'ITT', 'JBGS', 'JEF', 'JJC', 'JJM', 'JJU', 'JMEI', 'JOF', 'JPI', 'JPS', 'JQC', 'KBH', 'KHC', 'KLAC', 'KMX', 'KREF', 'KZIA', 'LAC', 'LBRDK', 'LCNB', 'LEGH', 'LEN', 'LGI', 'LMNX', 'LMPX', 'LND', 'LPLA', 'LSXMB', 'LVGO', 'LW', 'MANU', 'MCB', 'MCI', 'MDJH', 'MEET', 'MFC', 'MGP', 'MGTX', 'MGYR', 'MIME', 'MINI', 'MLI', 'MMX', 'MNSB', 'MPWR', 'MRBK', 'MRSN', 'MS', 'MTBC', 'MTLS', 'MYRG', 'NERV', 'NGHCO', 'NGVC', 'NKSH', 'NL', 'NNVC', 'NRIM', 'NSC', 'NSIT', 'NYCB', 'OMC', 'OMER', 'ONB', 'OPBK', 'OPNT', 'OPY', 'ORAN', 'ORLY', 'ORMP', 'OSIS', 'OSMT', 'OXLCM', 'OXSQL', 'OXSQZ', 'PAYX', 'PCF', 'PCN', 'PDLI', 'PEAK', 'PEBK', 'PEG', 'PETQ', 'PFBC', 'PFBI', 'PFE', 'PKO', 'PLAG', 'PLBC', 'PNC', 'POST', 'POWI', 'PPL', 'PRAH', 'PRIM', 'PROV', 'PRPL', 'PTCT', 'PVG', 'PXLW', 'QADB', 'QTRX', 'QURE', 'RBB', 'RBC', 'RCI', 'REGN', 'RELV', 'RFI', 'RILYO', 'RILYZ', 'RIO', 'RJF', 'RLI', 'RMT', 'RRBI', 'RUSHA', 'RUSHB', 'RYN', 'SAL', 'SALT', 'SBBX', 'SCHW', 'SF', 'SGG', 'SGH', 'SI', 'SIGI', 'SIM', 'SJI', 'SJR', 'SMBC', 'SNX', 'SON', 'SPKEP', 'SPWH', 'SPXX', 'SRDX', 'STND', 'STRL', 'STT', 'SVMK', 'SYNH', 'TAK', 'TANNI', 'TANNL', 'TANNZ', 'TARA', 'TBBK', 'TBIO', 'TCBK', 'TCMD', 'TCRW', 'TD', 'TEAM', 'TEL', 'TIVO', 'TK', 'TMUS', 'TPX', 'TRC', 'TRMB', 'TRS', 'TSLF', 'TT', 'TTEK', 'TWTR', 'UBS', 'UBX', 'UG', 'UHAL', 'UTF', 'UVV', 'VEEV', 'VICI', 'VOD', 'VRTS', 'VVR', 'WD', 'WIT', 'WPC', 'WSM', 'WTBA', 'WVFC', 'XRAY', 'YVR', 'ZEN', 'ZIONP'],
    (0.05) : 29,
}


FULL_SOLUTION = {
        "SMALL_FULL_SOLUTION" : (SMALL_FULL_SOLUTION, "data/small_dataset.txt"),
        "MEDIUM_FULL_SOLUTION" : (MEDIUM_FULL_SOLUTION, "data/medium_dataset.txt"),
        "LARGE_FULL_SOLUTION" : (LARGE_FULL_SOLUTION, "data/large_dataset.txt"),
}