# vllm-project/vllm#31080: [Bug]: TypeError: Received a CachedQwen2TokenizerFast for argument tokenizer

| 字段 | 值 |
| --- | --- |
| Issue | [#31080](https://github.com/vllm-project/vllm/issues/31080) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: TypeError: Received a CachedQwen2TokenizerFast for argument tokenizer

### Issue 正文摘录

### Your current environment - requirements ```bash torch 2.8.0+cu128 torch_memory_saver 0.0.8 torchao 0.9.0 torchaudio 2.8.0+cu128 torchdata 0.11.0 torchvision 0.23.0+cu128 transformer_engine 2.6.0+torch2.8.0cu128 transformers 4.57.1 vllm 0.11.0 ``` ### 🐛 Describe the bug Using a newly installed vllm and transformers results in the following error: "TypeError: Received a CachedQwen2TokenizerFast for argument tokenizer, but a ('Qwen2Tokenizer', 'Qwen2TokenizerFast') was expected." I've tried transformers versions 4.57.0 to 4.57.3, but the problem persists. - code ```python import os from transformers import AutoProcessor from vllm import LLM, SamplingParams import random import base64 random.seed(1) os.environ["VLLM_WORKER_MULTIPROC_METHOD"] = "spawn" def encode_image(image_path): with open(image_path, "rb") as image_file: return base64.b64encode(image_file.read()).decode('utf-8') if __name__ == "__main__": model_path = 'Qwen3-VL-4B-Instruct' processor = AutoProcessor.from_pretrained(model_path) llm = LLM( model=model_path, limit_mm_per_prompt={"image": 8}, tensor_parallel_size=2, gpu_memory_utilization=0.8, max_model_len=15000, ) ``` - error ```bash Traceback (most recent call la...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: TypeError: Received a CachedQwen2TokenizerFast for argument tokenizer bug;stale ### Your current environment - requirements ```bash torch 2.8.0+cu128 torch_memory_saver 0.0.8 torchao
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: 0.11.0 ``` ### 🐛 Describe the bug Using a newly installed vllm and transformers results in the following error: "TypeError: Received a CachedQwen2TokenizerFast for argument tokenizer, but a ('Qwen2Tokenizer', 'Qwen2Toke...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: gistry.py", line 143, in get_max_tokens_per_item_by_modality return profiler.get_mm_max_contiguous_tokens( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/mnt/bn/codebase/conda_env/source/envs/verl/lib/python3.12/site-pac...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ypeError: Received a CachedQwen2TokenizerFast for argument tokenizer bug;stale ### Your current environment - requirements ```bash torch 2.8.0+cu128 torch_memory_saver 0.0.8 torchao 0.9.0 torchaudio
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
