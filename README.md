# Stable Diffusion web UI
A browser interface based on Gradio library for Stable Diffusion.

![](screenshot.png)

## Các Tính Năng chính 
[Detailed feature showcase with images](https://github.com/AUTOMATIC1111/stable-diffusion-webui/wiki/Features):
1. Txt2Img (viết một đoạn text mô tả để sinh ra hình ảnh tương ứng) - ControlNet (Tạo ra các bức ảnh hoàn chỉnh từ các hình thái, đường nét ảnh từ người dùng đưa ra)
2. Img2Img (Sinh ra hình ảnh có những nét giống tương tự với ảnh của người dùng tải lên)
3. Inpaint (Mô hình sẽ chỉnh sửa các góc cạnh của bức ảnh (một khu vực của ảnh theo ý muốn của người dùng mô tả))
4. Img2Txt (Sinh ra các đoạn văn bản mô tả ảnh người dùng upload lên)
5. Train Lora (Tạo ra một mô hình các nhân hóa theo ý người dùng)


## Chi Tiết Các Tính Năng chính 
1. Txt2Img - ControlNet
A. Txt2Img
- Tạo ra hình ảnh từ mô tả người dùng nhập vào (Generate)
- Tạo ra văn bản gợi ý cho người dùng (Generate Prompt)
- Hộp Negative prompt là mục mình sẽ nhập những thứ không muốn xuất hiện trong bức ảnh sinh ra.
- Chỉnh sửa kích thước, tỉ lệ của bức ảnh được sinh ra.
B. ControlNet
- Hoàn thiện bức ảnh từ những nét phác thảo có sẵn.
- Trích xuất ra các khung, đường nét có trong bức ảnh người dùng tải lên (Ví dụ như )
- Để cài đặt ControlNet: Extensions => Install from URL => Gán https://github.com/lllyasviel/ControlNet.git => Installed => Tích => Apply and restart UI => Sử dụng
2. Img2Img 
- Tải bất kỳ một bức ảnh nào lên và sinh ra các hình ảnh có nét tương tự như vậy.
- Chèn thêm các đoạn văn bản mô tả bức ảnh mới được sinh ra.
3. Inpaint
- Ví dụ như nếu bạn muốn chỉnh góc bên trên tay trái là một bình hoa thì bạn sẽ bôi vào khu vực muốn đặt bình hoa và mô tả bình hoa
đó vào hộp text và sẽ cho ra một bức ảnh như mong muốn.
4. Img2Text 
- Đơn giản khi người dùng thích một bức ảnh nào đó mà không biết mô tả nó như nào thì mô hình sẽ giải quyết vấn đề này
- Tải ảnh lên => Generate text
5. Train Lora làm theo hướng dẫn tại đây https://www.youtube.com/watch?v=70H03cv57-o    

## Các cài đặt Stable Diffusion UI
1. Clone from https://github.com/NHD-TQ/UI_V2.git
2. Run file webui.bat
