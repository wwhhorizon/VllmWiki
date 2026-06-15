# vllm-project/vllm#17757: [Usage]: 使用vllm部署deepseek-vl2-tiny，无法一次请求包含两张图片

| 字段 | 值 |
| --- | --- |
| Issue | [#17757](https://github.com/vllm-project/vllm/issues/17757) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: 使用vllm部署deepseek-vl2-tiny，无法一次请求包含两张图片

### Issue 正文摘录

### Your current environment vllm版本：0.7.3 运行命令：python3 -m vllm.entrypoints.openai.api_server --model /data/LLM-project/deepseek-vl2/model/deepseek-ai/deepseek-vl2-tiny --served-model-name deepseek_vl2 --chat-template /data/LLM-project/deepseek-vl2/template_deepseek_vl2.jinja --hf-overrides '{"architectures": ["DeepseekVLV2ForCausalLM"]}' 请求示例： { "model": "deepseek_vl2", "messages": [ {"role": "system", "content": "你是一个有用的助手。"}, {"role": "user", "content": [ {"type": "image_url", "image_url": { "url": "xx./1-2.jpg"} }, {"type": "image_url", "image_url": { "url": "xx./2-2.jpg"} }, {"type": "text", "text": "上面两张图片是有关分光器的图片，判断是否为重复图片，注意：根据分光器的外观，以及光纤的插入端口来判断，光纤插入的端口不同属于不重复图片，输出要求：是重复图片：1，不是重复图片：0，不要输出其他内容"} ] } ] } 输出： { "object": "error", "message": "At most 1 image(s) may be provided in one request.", "type": "BadRequestError", "param": null, "code": 400 } 在deepseek官网查看示例，tiny模型应该是支持同时上传多张图片的，请问这是template_deepseek_vl2.jinja模版的问题吗 ### How would you like to use vllm ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: nment vllm版本：0.7.3 运行命令：python3 -m vllm.entrypoints.openai.api_server --model /data/LLM-project/deepseek-vl2/model/deepseek-ai/deepseek-vl2-tiny --served-model-name deepseek_vl2 --chat-template /data/LLM-project/deepsee...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: a/LLM-project/deepseek-vl2/template_deepseek_vl2.jinja --hf-overrides '{"architectures": ["DeepseekVLV2ForCausalLM"]}' 请求示例： { "model": "deepseek_vl2", "messages": [ {"role": "system", "content": "你是一个有用的助手。"}, {"role":...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: ect": "error", "message": "At most 1 image(s) may be provided in one request.", "type": "BadRequestError", "param": null, "code": 400 } 在deepseek官网查看示例，tiny模型应该是支持同时上传多张图片的，请问这是template_deepseek_vl2.jinja模版的问题吗 ### How...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
