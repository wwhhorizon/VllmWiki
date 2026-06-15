# vllm-project/vllm#24652: [Feature]: vLLM serve batch inference (Multiple image or multiple prompt execution in sinlge request)

| 字段 | 值 |
| --- | --- |
| Issue | [#24652](https://github.com/vllm-project/vllm/issues/24652) |
| 状态 | closed |
| 标签 | feature request |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: vLLM serve batch inference (Multiple image or multiple prompt execution in sinlge request)

### Issue 正文摘录

### 🚀 The feature, motivation and pitch input_file1 = "1.jpg" input_file2 = "2.jpg" def conv_base64(input_file): import base64 # Read the image in binary mode and encode to base64 with open(input_file, "rb") as img_file: base64_str = base64.b64encode(img_file.read()).decode('utf-8') return base64_str data_uri_1 = f"data:image/jpeg;base64,{conv_base64(input_file1)}" data_uri_2 = f"data:image/jpeg;base64,{conv_base64(input_file2)}" response_2 = client.chat.completions.create( model=model_name, messages=[ {"role": "system", "content": sys_prompt}, { "role": "user", "content": [ {"type": "text", "text": user_prompt}, {"type": "image_url", "image_url": {"url": data_uri_1}}, {"type": "image_url", "image_url": {"url": data_uri_2}}, ], }, ], temperature=0, top_p=1, ) I got response only for single image.

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: e batch inference (Multiple image or multiple prompt execution in sinlge request) feature request ### 🚀 The feature, motivation and pitch input_file1 = "1.jpg" input_file2 = "2.jpg" def conv_base64(input_file): import b...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: _file1 = "1.jpg" input_file2 = "2.jpg" def conv_base64(input_file): import base64 # Read the image in binary mode and encode to base64 with open(input_file, "rb") as img_file: base64_str = base64.b64encode(img_file.read...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: _base64(input_file2)}" response_2 = client.chat.completions.create( model=model_name, messages=[ {"role": "system", "content": sys_prompt}, { "role": "user", "content": [ {"type": "text", "text": user_prompt}, {"

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
