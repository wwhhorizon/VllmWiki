# vllm-project/vllm#31337: [Bug]: Failed to capture CUDA kernel data and GPU memory data when running vllm with tensor_parallel_size=1

| 字段 | 值 |
| --- | --- |
| Issue | [#31337](https://github.com/vllm-project/vllm/issues/31337) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;kernel;operator;sampling;triton |
| 症状 | build_error;nan_inf |
| 根因提示 | env_dependency;shape |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Failed to capture CUDA kernel data and GPU memory data when running vllm with tensor_parallel_size=1

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Hi team, I'm trying to profile the performance of vllm using partial DeepSeekV3(only Layer 2 ~ 4 and embedding and lm_head layer). I just find that nsys profile failed to capture cuda kernel and memory data when I initialize the LLM class with the arg tensor_parallel_size=1. When I increase tensor_parallel_size to 2 or 4 or 8, it's okay. Here is my test script: ``` import time import datetime import torch from vllm import LLM, SamplingParams from transformers import AutoTokenizer DEFAULT_MODEL_PATH = "/mymodel/DeepSeek-V3-L2ToL4" def generate_prompts(tokenizer, batch_size, seq_len): torch.manual_seed(0) if tokenizer is None: tokenizer = AutoTokenizer.from_pretrained(DEFAULT_MODEL_PATH, trust_remote_code=True) dummy_input = torch.randint( low=3, # skip special tokens high=tokenizer.vocab_size, size=(batch_size, seq_len), ) dummy_output = tokenizer.batch_decode(dummy_input) return dummy_output def main(): model_name = "DeepSeek-V3-L2ToL4" model_path = f"/mymodels/{model_name}/" now = datetime.datetime.now() formatted_time = now.strftime('%Y%m%d_%H%M%S') output_steps = 16 seq_len = 1024 batchsize = 4 tokenizer = AutoTokenizer.from_p...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: or_parallel_size to 2 or 4 or 8, it's okay. Here is my test script: ``` import time import datetime import torch from vllm import LLM, SamplingParams from transformers import AutoTokenizer DEFAULT_MODEL_PATH = "/mymodel...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: port LLM, SamplingParams from transformers import AutoTokenizer DEFAULT_MODEL_PATH = "/mymodel/DeepSeek-V3-L2ToL4" def generate_prompts(tokenizer, batch_size, seq_len): torch.manual_seed(0) if tokenizer is None: tokeniz...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: r current environment ### 🐛 Describe the bug Hi team, I'm trying to profile the performance of vllm using partial DeepSeekV3(only Layer 2 ~ 4 and embedding and lm_head layer). I just find that nsys profile failed to cap...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug]: Failed to capture CUDA kernel data and GPU memory data when running vllm with tensor_parallel_size=1 bug;stale ### Your current environment ### 🐛 Describe the bug Hi team, I'm trying to profile the performance of...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ta and GPU memory data when running vllm with tensor_parallel_size=1 bug;stale ### Your current environment ### 🐛 Describe the bug Hi team, I'm trying to profile the performance of vllm using partial DeepSeekV3(only Lay...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
