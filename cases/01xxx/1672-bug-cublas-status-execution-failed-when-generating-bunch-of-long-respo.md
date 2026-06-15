# vllm-project/vllm#1672: [Bug] CUBLAS_STATUS_EXECUTION_FAILED when generating bunch of long responses

| 字段 | 值 |
| --- | --- |
| Issue | [#1672](https://github.com/vllm-project/vllm/issues/1672) |
| 状态 | closed |
| 标签 |  |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;gemm_linear;model_support;quantization;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;quantization |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug] CUBLAS_STATUS_EXECUTION_FAILED when generating bunch of long responses

### Issue 正文摘录

I am using vLLM to generate response from ChatGLM2 model. I found that when there are lots of queries and some of them cause the model to output very long responses. The program will raise CUDA error. In below example, the vLLM model is asked to handle 2000 quries with long response. Please note when using the default `max_len` of ChatGLM2 which is 8192, CUDA error are raised. But if we limit the `max_len` to 2048, or decrease the number of prompts, everything works fine. My env and env variable: - main branch of vLLM - torch 2.0.1 - huggingface 4.35 - cuda 12.2 - A100 GPUs - set CUDA_LAUNCH_BLOCKING to 1 ```python PATH_TO_CHATGLM2_6B = "THUDM/chatglm2-6b" PATH_TO_CHATGLM2_6B = "chatglm2-6b" # if model repo are cloned or linked here def test_vllm(prompts, max_tokens): from vllm import LLM, SamplingParams llm = LLM( model=PATH_TO_CHATGLM2_6B, tokenizer=PATH_TO_CHATGLM2_6B, trust_remote_code=True, tensor_parallel_size=1, ) sampling_params = SamplingParams(n=1, temperature=0.0, max_tokens=max_tokens) for i, p in enumerate(prompts): p = llm.get_tokenizer().build_prompt(p) prompts[i] = p responses = llm.generate(prompts, sampling_params=sampling_params) def process_response(response):...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: 2-6b" PATH_TO_CHATGLM2_6B = "chatglm2-6b" # if model repo are cloned or linked here def test_vllm(prompts, max_tokens): from vllm import LLM, SamplingParams llm = LLM( model=PATH_TO_CHATGLM2_6B, tokenizer=PATH_TO_CHATGL...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: nch of long responses I am using vLLM to generate response from ChatGLM2 model. I found that when there are lots of queries and some of them cause the model to output very long responses. The program will raise CUDA err...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: de=auto, revision=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.float16, max_seq_len=32768, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=None, seed=0) WARNING 11-15 15:3...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: em cause the model to output very long responses. The program will raise CUDA error. In below example, the vLLM model is asked to handle 2000 quries with long response. Please note when using the default `max_len` of Ch...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: torch 2.0.1 - huggingface 4.35 - cuda 12.2 - A100 GPUs - set CUDA_LAUNCH_BLOCKING to 1 ```python PATH_TO_CHATGLM2_6B = "THUDM/chatglm2-6b" PATH_TO_CHATGLM2_6B = "chatglm2-6b" # if model repo are cloned or linked here de...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
