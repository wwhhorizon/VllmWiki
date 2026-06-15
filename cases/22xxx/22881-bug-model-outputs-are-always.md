# vllm-project/vllm#22881: [Bug]: Model outputs are always '!!!!!!!!!!!!!!'

| 字段 | 值 |
| --- | --- |
| Issue | [#22881](https://github.com/vllm-project/vllm/issues/22881) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 14; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;fp8;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Model outputs are always '!!!!!!!!!!!!!!'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python import os os.environ["VLLM_USE_V1"] = "1" os.environ["CUDA_VISIBLE_DEVICES"] = "0,1" os.environ["VLLM_USE_FLASHINFER_SAMPLER"] = "0" from vllm.config import CompilationConfig from vllm import LLM from transformers import AutoTokenizer model = "/data/pretrained_models/Qwen3-30B-A3B-Thinking-2507-FP8" tokenizer = AutoTokenizer.from_pretrained(model, trust_remote_code=True) config = CompilationConfig( level=3, compile_sizes=[1, 2, 4], # pass_config={ # "enable_async_tp": True, # } ) if __name__ == "__main__": llm = LLM( model=model, enforce_eager=True, tensor_parallel_size=2, enable_expert_parallel=True, compilation_config=config, max_model_len=1024, gpu_memory_utilization=0.9, enable_prefix_caching=True, enable_chunked_prefill=True, ) messages = [ {"role": "user", "content": "你叫什么名字"} ] prompt = tokenizer.apply_chat_template( messages, tokenize=False, add_generation_prompt=True, ) outputs = llm.generate(prompt) print("outputs:", outputs) ``` The output is ``` [RequestOutput(request_id=0, prompt=' user\n你叫什么名字 \n assistant\n \n', prompt_token_ids=[151644, 872, 198, 56568, 99882, 99245, 101419, 151645, 198, 151644, 77091, 1...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ' bug ### Your current environment ### 🐛 Describe the bug ```python import os os.environ["VLLM_USE_V1"] = "1" os.environ["CUDA_VISIBLE_DEVICES"] = "0,1" os.environ["VLLM_USE_FLASHINFER_SAMPLER"] = "0" from vllm.config i...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: oTokenizer model = "/data/pretrained_models/Qwen3-30B-A3B-Thinking-2507-FP8" tokenizer = AutoTokenizer.from_pretrained(model, trust_remote_code=True) config = CompilationConfig( level=3, compile_sizes=[1, 2, 4], # pass_...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Model outputs are always '!!!!!!!!!!!!!!' bug ### Your current environment ### 🐛 Describe the bug ```python import os os.environ["VLLM_USE_V1"] = "1" os.environ["CUDA_VISIBLE_DEVICES"] = "0,1" os.environ["VLLM_US...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: lization=0.9, enable_prefix_caching=True, enable_chunked_prefill=True, ) messages = [ {"role": "user", "content": "你叫什么名字"} ] prompt = tokenizer.apply_chat_template( messages, tokenize=False, add_generation_prompt=True,...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: "] = "1" os.environ["CUDA_VISIBLE_DEVICES"] = "0,1" os.environ["VLLM_USE_FLASHINFER_SAMPLER"] = "0" from vllm.config import CompilationConfig from vllm import LLM from transformers import AutoTokenizer model = "/data/pr...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
