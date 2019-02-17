Giới thiệu
----------

OpenCV (Open Computer Vision) là một thư viện mã nguồn mở chuyên dùng để xử lý các vấn đề liên quan đến thị giác máy tính. Nhờ một hệ thống các giải thuật chuyên biệt, tối ưu cho việc xử lý thị giác máy tính, vì vậy tính ứng dụng của OpenCV là rất lớn.

Xử lý ảnh là quá trình xử lý, thao tác hình ảnh để có một hình ảnh khác phù hợp với nhu cầu của người dùng,...

Tiền đề bài viết
----------------

Bài viết nằm trong loạt bài viết chương trình Tự Học OpenCV Qua Các Ví Dụ Thực Tế được tài trợ bởi [STDIO](https://www.stdio.vn/). Trong bài viết sẽ giới thiệu:

-   Khái niệm và kỹ thuật ảnh xám (Grayscale).
-   Ảnh nhị phân và nhị phân hóa (Adaptive Threshold).

Đối tượng hướng đến
-------------------

Bài viết hướng tới các bạn đọc mới tìm hiểu về xử lý ảnh, đặc biệt là với OpenCV và chưa có kiến thức tương đương.

GrayScale là gì?
----------------

-   Là một hệ thống màu có mô hình màu đơn giản nhất với 256 cấp độ xám biến thiên từ màu đen đến màu trắng.
-   Sản phẩm được xuất ra sẽ có màu trắng đen.
-   Được sử dụng cả trong công nghiệp in lẫn dùng trong việc thể hiện ảnh lên các thiết bị số.
-   Ảnh xám (Gray image) hay còn gọi là ảnh đơn sắc (Monochromatic), mỗi giá trị điểm ảnh (Pixel) trong ma trận điểm ảnh mang giá trị từ 0 đến 255.
-   Trong khôn gian màu RGB, để có một ảnh xám cần có phải có giá trị kênh màu Red(x, y) = Green(x, y) = Blue(x, y). (Với x,y lần lượt là tọa độ của điểm ảnh)![ss_1](https://www.stdio.vn/statics/external_data/files/pages/articles/2015/383/content/ss_1.png) 

Chuyển đổi hệ thống màu RGB sang Grayscale
------------------------------------------

Một bức ảnh mà tập hợp của một ma trận điểm ảnh(Pixel). Mỗi điểm ảnh có thể được biểu diễn bằng n bytes dưới các kênh màu khác nhau. Việc chuyển đổi giữa các hệ màu thông thường được thực hiện thông qua các phép biến đổi ma trận.

Trong bài viết này tôi sẽ giới thiệu cách chuyển đổi từ ảnh 24 bits RGB sang ảnh 8 bits Grayscale. Tôi có công thức tính cường độ sáng tại một điểm ảnh từ ảnh RGB.

  ```I(x, y)  =  0.3086  *  Red(x, y)  +  0.6094  *  Green(x, y)  +  0.0820  *  Blue(x, y)```
  
  ```I(x, y)  =  0.299  *  Red(x, y)  +  0.587  *  Green(x, y)  +  0.114  *  Blue(x, y)```

##### Phân tích

-   **I(x, y):** Là cường độ sáng tại điểm ảnh (x, y) của ảnh xám.
-   **Red(x, y)**: Là giá trị của kênh màu Red(Đỏ) tại điểm ảnh (x, y) của ảnh màu(RGB).
-   **Green(x, y):** Là giá trị của kênh màu Green(Xanh lá cây) tại điểm ảnh (x, y) của ảnh màu(RGB).
-   **Blue(x, y): **Là giá trị của kênh màu Blue(Xanh lơ) tại điểm ảnh (x, y) của ảnh màu(RGB).

Tôi có công thức khác tính cường độ sáng tại một điểm ảnh từ ảnh RGB.

  ```I(x, y)  =  (  2  *  Red(x, y)  +  5  *  Green(x, y)  +  1  *  Blue(x, y)  )  /  8```

##### Chú ý

-   Các phép toán trong số nguyên (Int) nhanh hơn rất nhiều trong số thực (Float).
-   Trong OpenCV, hệ thống màu có thứ tự các kênh màu là Blue-Green-Red. 
-   Các thông số dùng để tính toán cường độ sáng cho ảnh xám như: 0.3086, 0.6094, 0.0820,... được coi là những con số đẹp do người ta nghiên cứu ra. Các con số này có thể thay đổi. Bạn hoàn toàn có thể chọn một giá trị một kênh màu hoặc chia trung bình cộng của 3 kênh màu để tìm cường độ sáng tại một điểm ảnh (Pixel).

### Chuyển đổi ảnh xám trong OpenCV

Trong OpenCV, để chuyển một tấm ảnh có hệ màu RGB sang Graysacle, hay thậm chí là các không gian màu qua lại với nhau nhờ phương thức cvtColor() (Convert color). 

```cv::cvtColor(cv::InputArray src, cv::OutputArray dst,  int code)```

##### Phân tích

-   **src**: Là hình ảnh gốc (Trong bài viết này là ảnh màu).
-   **dst**: Là ảnh thu được (Trong bài viết này là ảnh xám).
-   **code**: Là mã chuyển màu. Ví dụ: code = CV_BGR2GRAY là chuyển đổi ảnh màu thành ảnh xám,...

##### Ví dụ

![ss_2](https://www.stdio.vn/statics/external_data/files/pages/articles/2015/383/content/ss_2.png)

Ảnh nhị phân
------------

-   Là ảnh mà giá trị của các điểm ảnh chỉ được biểu diễn bằng hai giá trị là 0 (Đen) và 255 (Trắng) (Tương ứng với 0 và 1, nhưng tôi vẫn để nguyên giá trị 0 và 255 để có thể hiểu hơn trong việc tính toán).
-   Vì giá trị của điểm ảnh được biểu diễn bởi 2 giá trị là 0 hoặc 1, nên một điểm ảnh được biểu diễn bằng 1 bit nên ảnh có kích thước rất nhỏ.

### Nhị phân hóa

Là quá trình biến đổi một ảnh xám thành ảnh nhị phân.

-   Tôi gọi giá trị cường độ sáng tại một điểm ảnh là I(x,y) .
-   INP(x,y) là cường độ sáng của điểm ảnh trên ảnh nhị phân .
-   (Với 0 < x < image.width) và (0 < y < image.height).

Để biến đổi ảnh xám thành ảnh nhị  phân. Ta so sánh giá trị cường độ sáng của điểm ảnh với một ngưỡng nhị phân **T**. 

-   Nếu I(x,y) > **T** thì INP(x, y) = 0 (0).
-   Nếu I(x,y) > **T** thì INP(x, y) = 255 (1).

##### Chú ý

-   Bạn có thể hoàn toàn chọn giá trị **T** từ 0 đến 255, nhưng thông thường nhiều người hay chọn một giá trị đó là 128 tức là giá trị trung bình của max(255) và min(0) của cường độ sáng (Intensity) của điểm ảnh.
-   Bạn có thể dễ dàng nhận thấy với mỗi **T** thì có một ảnh nhị phân khác nhau (Khác nhau ở đây là cường độ sáng của các tấm ảnh nhị phân với mỗi giá trị **T**).

Để có thể thu được ảnh nhị phân mà khi đó bạn không quan tâm tới cường độ sáng, có một kỹ thuật giúp bạn là nhị phân hóa ngưỡng động.

#### Nhị phân hóa trong OpenCV

Để chuyển một ảnh thành một ảnh nhị phân, sử dụng phương thức threshold().

  ```threshold(cv::InputArray src, cv::OutputArray dst,  double thresh,  double maxval,  int type);```

##### Phân tích

-   **src**: Là hình ảnh gốc (Trong bài viết này là ảnh màu).
-   **dst**: Là ảnh thu được (Trong bài viết này là ảnh nhị phân).
-   **thresh**: Là ngưỡng nhị phân **T**.
-   **maxval: **Là giá trị lớn nhất trong ảnh (maxval = 255 đối với ảnh xám).
-   **type**: Là kiểu nhị phân. 

##### Ví dụ
![ss_3](https://www.stdio.vn/statics/external_data/files/pages/articles/2015/383/content/ss_3.png)

### Nhị phân hóa ngưỡng động

Ý tưởng:

1.  Chia tấm ảnh thành nhiều khu vực, cửa sổ khác nhau (Region).
2.  Dùng một thuật toán để tìm một giá trị **T** phù hợp với từng khu vực, cửa sổ (Region).
3.  Áp dụng phương pháp nhị phân hóa cho từngkhu vực, cửa sổ (Region) với **T** phù hợp.

Điều quan trọng trong kĩ thuật này là phải tìm một giá trị **T** phù hợp với từng khu vực, cửa sổ (Region) hoặc cả tấm ảnh. Có rất nhiều phương pháp để tìm **T**, ở nội dung tiếp theo tôi sẽ giới thiệu một số thuật toán giúp tìm kiếm giá trị **T** này.

#### Thuật toán Otsu

**Bước 1:** Xác định T1. Giá trị cho T1 ban đầu nên chọn là (0+255) / 2 = 128.

**Bước 2:** Phân loại thành 2 nhóm điểm ảnh.  

-   Loại 1 **(**Type1): chứa tất cả các điểm ảnh có giá trị cường độ sáng (Intensity) <= **T**.    
-   Loại 2 (Type2): chứa tất cả các điểm ảnh có giá trị cường độ sáng (Intensity) > **T**.

**Bước 3:** Tính giá trị cường độ sáng trung bình (iAverage) cho Type1 (iAverage1) và Type2 (iAverage2).

**Bước 4:** Tính giá trị T2 theo công thức (iAverage1 + iAverage2) /2.

**Bước 5:** So sánh T1 và T2. 

-   Nếu giá trị chênh lệch của T1 và T2 <= Delta (một giá trị cho trước) thì T2 chính là **T** cần tìm. 
-   Nếu giá trị chênh lệch của T1 và T2 > Delta Deltal thì quay lại **Bước 1**.

![ss_4](https://www.stdio.vn/statics/external_data/files/pages/articles/2015/383/content/ss_4.png)

#### Thuật toán đối xứng

**Bước 1**:   Khởi tạo mảng Histogram (histogram). Tìm giá trị cường độ sáng (intensityMax) có tuần suất xuất hiện nhiều nhất histogram[intensityMax].

**Bước 2**: Duyệt toàn bộ các mức xám giảm từ 255 đến intensityMax. Nếu tại mức xám nào có tuần suất xuất hiện trên ảnh là 5% thì dừng lại. Lấy giá trị đối xứng qua histogram[intensityMax] là ngưỡng động **T**.

11. T = intensityMax -  (split - intensityMax);

![ss_5](https://www.stdio.vn/statics/external_data/files/pages/articles/2015/383/content/ss_5.png)

#### Thuật toán tam giác

**Bước 1:** Khởi tạo mảng Histogram (histogram).

-   Tìm giá trị intensityMax và histogram[intensityMax]. 
-   Tìm giá trị intensityMin và histogram[intensittyMin].    

**Bước 2:** Duyệt toàn bộ các mức xám từ intensityMin đến intensityMax . Tính khoảng cách tương ứng sau đó xét ngưỡng **T** bằng giá trị mức xám có khoảng cách lớn nhất. 

##### Phân tích

Phương thức findDistance(Point a, Point b, Point c) là tìm khoảng cách từ một điểm đến một đường thẳng với các tham số:

-   **a **và **b**: Lần lượt là 2 điểm khác biệt trên đường thẳng.
-   **c**: là điểm cần tìm khoảng cách tới đường thẳng.

![ss_6](https://www.stdio.vn/statics/external_data/files/pages/articles/2015/383/content/ss_6.png)

#### Nhị phân hóa ngưỡng động trong OpenCV

Để chuyển một ảnh thành một ảnh nhị phân, sử dụng phương thức adaptiveThreshold()

```adaptiveThreshold(cv::InputArray src, cv::OutputArray dst,  double maxValue,```

```int adaptiveMethod,  int thresholdType,  int blockSize,  double C);```

##### Phân tích

-   **src**: Là hình ảnh gốc (Trong bài viết này là ảnh màu).
-   **dst**: Là ảnh thu được (Trong bài viết này là ảnh nhị phân).
-   **thresh**: Là ngưỡng nhị phân **T**.
-   **maxValue: **Là giá trị lớn nhất trong ảnh (maxval = 255 đối với ảnh xám).
-   **adaptiveMethod**: Là cách thức nhị phân với ngưỡng động, nó chính là cách tính giá trị ngưỡng nhị phân trong từng vùng cần nhị phân.
-   **thresholdType**: Là kiểu nhị phân. 
-   **blockSize**: Là kích thước của cửa sổ (Region) áp dụng cho việc tính toán ngưỡng động (bạn nên chọn các giá trị %3 = 0 || %5 = 0 || %7 = 0).
-   **C**: Là một thông số để bù trừ trong trường hợp ảnh có độ tương phản quá lớn.

##### Ví dụ

![ss_7](https://www.stdio.vn/statics/external_data/files/pages/articles/2015/383/content/ss_7.png)
