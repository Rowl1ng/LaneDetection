# LaneDetection
[我的记录](http://rowl1ng.com/lanedetection/)
Process the lane images to get white/black images : the lane mark is white while other parts are black.
## 一、需求
1. 总体需求
对CiCS设备采集的路面图像中的道路标志标线进行识别及位置标记。
2. 路面图像
路面图像包括CiCS两种照明模式下的图片，需要对两种照明下的标线进行识别，尽可能统一一个接口调用执行，如一个算法有困难，可通过参数调用不同算法针对不同照明图像。
3. 标线识别结果标记
[ ]生成一个新的大小与输入图像一致的图像，在新图像中对识别出的标线像素用白色灰度（255）表示，对于其余位置像素用黑色表示（0）。
4. 识别要求
1）标线上的开裂裂缝算作标线的一部分，需要算作标线整体的一部分，不能分成小块识别出。
2）标线由于光照条件及自身颜色，在灰度上会有不同标线，要求能自适应各种灰度分布下的标线。
3）对于污损或磨损严重的标线，要求能够尽可能的将标线识别的完整。

## 二、指标
对于正常的洁净的路面图像上无明显或轻微污损的标志标线，要求识别的完整性>=80%。
对于污损较严重的标线，要求对无污损的部分能完整识别（>=80%），污损的部分尽可能补全。
