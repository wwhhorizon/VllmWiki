# vllm-project/vllm#2435: cuda11.8 use gptq for Qwen

| 字段 | 值 |
| --- | --- |
| Issue | [#2435](https://github.com/vllm-project/vllm/issues/2435) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | frontend_api;model_support;quantization;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;quantization;sampling |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> cuda11.8 use gptq for Qwen

### Issue 正文摘录

Hi , my env is cuda 118 , and my model is qwen int4. my vllm install https://github.com/vllm-project/vllm/releases/download/v0.2.7/vllm-0.2.7+cu118-cp310-cp310-manylinux1_x86_64.whl my code is : model_path = "/mnt/e/weight/MODELSCOPE/qwen/gptq0113" llm = LLM(model=model_path, tensor_parallel_size=1,trust_remote_code=True) sampling_params = SamplingParams(temperature=0.8, top_p=0.95) prompts = [query] outputs = llm.generate(prompts, sampling_params) response = outputs[0].outputs[0].text but the result is error!!! for example: input is :hello output is :username_0: Hello again! I have a problem using your API. I input:tell me all about bejing output:The answer to the question is not provided in the given text. Therefore, I can you help me ? thanks

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: da11.8 use gptq for Qwen Hi , my env is cuda 118 , and my model is qwen int4. my vllm install https://github.com/vllm-project/vllm/releases/download/v0.2.7/vllm-0.2.7+cu118-cp310-cp310-manylinux1_x86_64.whl my code is :...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: cuda11.8 use gptq for Qwen Hi , my env is cuda 118 , and my model is qwen int4. my vllm install https://github.com/vllm-project/vllm/releases/download/v0.2.7/vllm-0.2.7+cu118-cp310-cp310-manylinux1_x86_64.whl my code is...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: for Qwen Hi , my env is cuda 118 , and my model is qwen int4. my vllm install https://github.com/vllm-project/vllm/releases/download/v0.2.7/vllm-0.2.7+cu118-cp310-cp310-manylinux1_x86_64.whl my code is : model_path = "/...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: cuda11.8 use gptq for Qwen Hi , my env is cuda 118 , and my model is qwen int4. my vllm install https://github.com/vllm-project/vllm/releases/download/v0.2.7/vllm-0.2.7+cu118-cp310-cp310-manylinux1_x86_64.whl my cod

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
