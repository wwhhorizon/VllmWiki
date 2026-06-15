# vllm-project/vllm#4168: [Bug]:  vllm how to load Yarn-Mistral-7B-128k(24G 4090, maybe max-model-len*black-size limits max-seq-len) 

| 字段 | 值 |
| --- | --- |
| Issue | [#4168](https://github.com/vllm-project/vllm/issues/4168) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  vllm how to load Yarn-Mistral-7B-128k(24G 4090, maybe max-model-len*black-size limits max-seq-len) 

### Issue 正文摘录

### Your current environment ```text Versions of relevant libraries: [pip3] clip-anytorch==2.5.2 [pip3] mypy-extensions==1.0.0 [pip3] numpy==1.23.5 [pip3] onnx==1.14.0 [pip3] onnxruntime==1.16.3 [pip3] onnxruntime-gpu==1.16.3 [pip3] open-clip-torch==2.20.0 [pip3] pytorch-lightning==1.9.4 [pip3] torch==2.1.2 [pip3] torchdiffeq==0.2.3 [pip3] torchmetrics==0.11.4 [pip3] torchsde==0.2.6 [pip3] torchvision==0.15.1+cu118 [pip3] triton==2.1.0 [conda] clip-anytorch 2.5.2 pypi_0 pypi [conda] numpy 1.23.5 pypi_0 pypi [conda] open-clip-torch 2.20.0 pypi_0 pypi [conda] pytorch-lightning 1.9.4 pypi_0 pypi [conda] torch 2.1.2 pypi_0 pypi [conda] torchdiffeq 0.2.3 pypi_0 pypi [conda] torchmetrics 0.11.4 pypi_0 pypi [conda] torchsde 0.2.6 pypi_0 pypi [conda] torchvision 0.15.1+cu118 pypi_0 pypi [conda] triton 2.1.0 pypi_0 pypiROCM Version: Could not collect Neuron SDK Version: N/A vLLM Version: 0.4.0.post1 ``` ### 🐛 Describe the bug ## code ``` from vllm import LLM, SamplingParams prompts = [ "hello, who is you?", ] sampling_params = SamplingParams(temperature=0.8, top_p=0.95) llm = LLM(model="TheBloke/Yarn-Mistral-7B-128k-GPTQ", ) outputs = llm.generate(prompts, sampling_params) for output in ou...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: s==0.11.4 [pip3] torchsde==0.2.6 [pip3] torchvision==0.15.1+cu118 [pip3] triton==2.1.0 [conda] clip-anytorch 2.5.2 pypi_0 pypi [conda] numpy 1.23.5 pypi_0 pypi [conda] open-clip-torch 2.20.0
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ize limits max-seq-len) bug;stale ### Your current environment ```text Versions of relevant libraries: [pip3] clip-anytorch==2.5.2 [pip3] mypy-extensions==1.0.0 [pip3] numpy==1.23.5 [pip3] onnx==1.14.0 [pip3] onnxruntim...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: B-128k(24G 4090, maybe max-model-len*black-size limits max-seq-len) bug;stale ### Your current environment ```text Versions of relevant libraries: [pip3] clip-anytorch==2.5.2 [pip3] mypy-extensions==1.0.0 [pip3] numpy==...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: del, tokenizer, tokenizer_mode, trust_remote_code, tensor_parallel_size, dtype, quantization, revision, tokenizer_revision, seed, gpu_memory_utilization, swap_space, enforce_eager, max_context_len_to_capture, disable_cu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: vllm how to load Yarn-Mistral-7B-128k(24G 4090, maybe max-model-len*black-size limits max-seq-len) bug;stale ### Your current environment ```text Versions of relevant libraries: [pip3] clip-anytorch==2.5.2 [pip3]...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
