Sử dụng OpenCV trong bài toán nhận diện khuôn mặt
-------------------------------------------------

Thật ra thuật toán ở đây đã được viết sẵn hết rồi, đúc kết ở tập tin XML cascades. Bỏ vào thôi, ta sẽ dùng 
```xml
haarcascade_frontal**face**_default.xml
```

Bước 1: Đầu vào sẽ là bức ảnh và tệp tin xml

```python
image = cv2.imread("images/JunVu.jpg")
face_cascade = cv2.CascadeClassifier("cascade_frontface.xml")
```

Bước 2: Tạo một bức ảnh xám từ bức ảnh gốc

```python
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```

Bước 3: Sử dụng phương thức detectMultiScale để phát hiện khuôn mặt trong bức ảnh xám

```python
faces = faceCascade.detectMultiScale(
grayImage,
scaleFactor =  1.1,
minNeighbors =  5,
minSize=(20, 20)
)
```

-   Tham số thứ nhất là nguồn/bức ảnh xám.
-   scaleFactor: độ scale sau mỗi lần quét, tính theo **0.01 = 1%**. Nếu như để scaleFactor = 1 thì tấm ảnh sẽ giữ nguyên
-   minNeighbors: scale và quét ảnh cho đến khi không thể scale được nữa thì lúc này sẽ xuất hiện những khung ảnh trùng nhau, số lần trùng nhau chính là tham số minNeighbors để quyết định cho việc có chọn khung ảnh này là khuôn mặt hay không.
-   minSize: cái tên nói lên tất cả rồi.

> Ngoài ra còn có các tham số như là maxScale, minScale để cho kích thước khung ảnh bắt đầu và kích thước khung ảnh kết thúc.
>
> Có thể hiệu chỉnh tham số scaleFactor, minNeighbors, minScale, maxScale để có kết quả như mong muốn.

Bước 4: Sau khi tính toán thì dữ liệu các khuôn mặt đã có trong biến faces, để muốn xác thực chúng ta vẽ nó lên bức ảnh gốc và phác họa ra màn hình

```python
# Draw
for  (x, y, w, h)  in faces:
cv2.rectangle(image,  (x, y),  (x+w, y+h),  (0,  255,  0),  2)
# Show
cv2.imshow("Faces found", image)
```