# vllm-project/vllm#15209: [Bug]: can't cache image embeds input

| 字段 | 值 |
| --- | --- |
| Issue | [#15209](https://github.com/vllm-project/vllm/issues/15209) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;multimodal_vlm;sampling_logits |
| 子分类 | install |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: can't cache image embeds input

### Issue 正文摘录

### Your current environment torch==2.6.0 transformers==4.40.2 ### 🐛 Describe the bug if the input of image is a embeds tensor like this. the cache module will get a error ``` sampling_params = SamplingParams(temperature=0.0, max_tokens=128, stop_token_ids = [tokenizer.eos_token_id], ) image_data = [torch.randn(2, 1536).cuda().to(torch.bfloat16)] # image_data = [] outputs = llm.generate( {"prompt": prompt, "multi_modal_data": { "image": image_data } }, sampling_params=sampling_params) print(outputs[0].outputs) ``` ![Image](https://github.com/user-attachments/assets/3f7d53f1-6e3a-4733-bb6e-2f6c87a73bb6) The issue occurs in the hasher.py module: when hashing a tensor, you need to first move it to the CPU and then convert it to a NumPy array. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ) image_data = [torch.randn(2, 1536).cuda().to(torch.bfloat16)] # image_data = [] outputs = llm.generate( {"prompt": prompt, "multi_modal_data": { "image": image_data } }, sampling_params=sampling_params) print(outputs[...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ) image_data = [torch.randn(2, 1536).cuda().to(torch.bfloat16)] # image_data = [] outputs = llm.generate( {"prompt": prompt, "multi_modal_data": { "image": image_data } }, sampling_params=sampling_params)
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: can answer lots of frequently asked questions. development frontend_api;multimodal_vlm;sampling_logits cuda dtype;env_dependency Your current environment
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: . development frontend_api;multimodal_vlm;sampling_logits cuda dtype;env_dependency Your current environment
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: can't cache image embeds input bug;stale ### Your current environment torch==2.6.0 transformers==4.40.2 ### 🐛 Describe the bug if the input of image is a embeds tensor like this. the cache module will get a error...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
