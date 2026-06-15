# vllm-project/vllm#2580: RuntimeError on ROCm

| 字段 | 值 |
| --- | --- |
| Issue | [#2580](https://github.com/vllm-project/vllm/issues/2580) |
| 状态 | closed |
| 标签 | rocm |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | attention;cuda;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> RuntimeError on ROCm

### Issue 正文摘录

Example of command: ```python benchmark_throughput.py --model gpt2 --input-len 256 --output-len 256``` Output: ```Namespace(backend='vllm', dataset=None, input_len=256, output_len=256, model='gpt2', tokenizer='gpt2', quantization=None, tensor_parallel_size=1, n=1, use_beam_search=False, num_prompts=1000, seed=0, hf_max_batch_size=None, trust_remote_code=False, max_model_len=None, dtype='auto', enforce_eager=False) INFO 01-24 14:52:52 llm_engine.py:72] Initializing an LLM engine with config: model='gpt2', tokenizer='gpt2', tokenizer_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=1024, download_dir=None, load_format=auto, tensor_parallel_size=1, quantization=None, enforce_eager=False, seed=0) WARNING[XFORMERS]: xFormers can't load C++/CUDA extensions. xFormers was built for: PyTorch 2.1.1+cu121 with CUDA 1201 (you have 2.3.0.dev20240123+rocm5.7) Python 3.10.13 (you have 3.10.13) Please reinstall xformers (see https://github.com/facebookresearch/xformers#installing-xformers) Memory-efficient attention, SwiGLU, sparse and more won't be available. Set XFORMERS_MORE_DETAILS=1 for more details INFO 01-24 14:52:55 weight_utils....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: 0.dev20240123+rocm5.7) Python 3.10.13 (you have 3.10.13) Please reinstall xformers (see https://github.com/facebookresearch/xformers#installing-xformers) Memory-efficient attention, SwiGLU, sparse and more won't be avai...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: ror on ROCm rocm Example of command: ```python benchmark_throughput.py --model gpt2 --input-len 256 --output-len 256``` Output: ```Namespace(backend='vllm', dataset=None, input_len=256, output_len=256, model='gpt2', tok...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: RuntimeError on ROCm rocm Example of command: ```python benchmark_throughput.py --model gpt2 --input-len 256 --output-len 256``` Output: ```Namespace(backend='vllm', dataset=None, input_len=256, output_len=256, model='g...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 4: RuntimeError on ROCm rocm Example of command: ```python benchmark_throughput.py --model gpt2 --input-len 256 --output-len 256``` Output: ```Namespace(backend='vllm', dataset=None, input_len=256, output_len=256, model='g...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: set=None, input_len=256, output_len=256, model='gpt2', tokenizer='gpt2', quantization=None, tensor_parallel_size=1, n=1, use_beam_search=False, num_prompts=1000, seed=0, hf_max_batch_size=None, trust_remote_code=False,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
