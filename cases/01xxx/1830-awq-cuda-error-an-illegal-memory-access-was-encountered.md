# vllm-project/vllm#1830: awq CUDA error: an illegal memory access was encountered

| 字段 | 值 |
| --- | --- |
| Issue | [#1830](https://github.com/vllm-project/vllm/issues/1830) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | attention_kv_cache;ci_build;frontend_api;gemm_linear;model_support;quantization;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;quantization;sampling |
| 症状 | build_error;crash;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> awq CUDA error: an illegal memory access was encountered

### Issue 正文摘录

hi, I get an "an illegal memory access was encountered" error when inference [deepseek-coder-33B-base-AWQ](https://huggingface.co/TheBloke/deepseek-coder-33B-base-AWQ), which is a Llama2 (GQA) architecture model, but the smaller model is fine([deepseek-coder-6.7B-base-AWQ](https://huggingface.co/TheBloke/deepseek-coder-6.7B-base-AWQ)), the relevant information as follows: ## Environment python==3.8 torch==2.0.1+cu118 transformers==4.34.1 vllm==0.2.2 ## Code ```` from vllm import LLM, SamplingParams import torch model_path = "deepseek-coder-33b-base-awq" sampling_params = SamplingParams(temperature=0.0, n=1, use_beam_search=False, top_p=1, top_k=-1, max_tokens=200, skip_special_tokens=False, stop_token_ids=stop_token_ids) llm = LLM(model=model_path, quantization="awq", dtype="auto", gpu_memory_utilization=0.9, swap_space=32) text = "def quick_sort(" outputs = llm.generate([text], sampling_params) print(outputs) ```` ## Error ```` INFO 11-29 16:37:53 llm_engine.py:72] Initializing an LLM engine with config: model='deepseek-coder-33b-base-awq', tokenizer='deepseek-coder-33b-base-awq', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.fl...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ch==2.0.1+cu118 transformers==4.34.1 vllm==0.2.2 ## Code ```` from vllm import LLM, SamplingParams import torch model_path = "deepseek-coder-33b-base-awq" sampling_params = SamplingParams(temperature=0.0, n=1, use
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: encountered" error when inference [deepseek-coder-33B-base-AWQ](https://huggingface.co/TheBloke/deepseek-coder-33B-base-AWQ), which is a Llama2 (GQA) architecture model, but the smaller model is fine([deepseek-coder-6.7...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: stop_token_ids=stop_token_ids) llm = LLM(model=model_path, quantization="awq", dtype="auto", gpu_memory_utilization=0.9, swap_space=32) text = "def quick_sort(" outputs = llm.generate([text], sampling_params) print(outp...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: awq CUDA error: an illegal memory access was encountered hi, I get an "an illegal memory access was encountered" error when inference [deepseek-coder-33B-base-AWQ](https://huggingface.co/TheBloke/deepseek-coder-33B-base...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: n=1, use_beam_search=False, top_p=1, top_k=-1, max_tokens=200, skip_special_tokens=False, stop_token_ids=stop_token_ids) llm =

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
