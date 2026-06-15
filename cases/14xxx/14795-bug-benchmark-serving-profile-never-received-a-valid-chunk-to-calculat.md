# vllm-project/vllm#14795: [Bug]: benchmark_serving  --profile  Never received a valid chunk to calculate TTFT.This response will be marked as failed!

| 字段 | 值 |
| --- | --- |
| Issue | [#14795](https://github.com/vllm-project/vllm/issues/14795) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;triton |
| 症状 | slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: benchmark_serving  --profile  Never received a valid chunk to calculate TTFT.This response will be marked as failed!

### Issue 正文摘录

### Your current environment python3 benchmark_serving.py \ --model /workspace/models/DeepSeek-V2-Lite-Chat \ --host 0.0.0.0 \ --port 8001 \ --dataset-name random \ --num-prompts 1000 \ --random-input-len 1000 \ --random-output-len 10000 \ --profile \ --max-concurrency 32 > vllm_random-10000_triton$(date +%Y%m%d-%H%M).log 2>&1 & using --profile parameter take error RequestFuncOutput(generated_text='', success=False, latency=0.0, output_tokens=0, ttft=0.0, itl=[], tpot=0.0, prompt_len=1000, error='Never received a valid chunk to calculate TTFT.This response will be marked as failed!') ### 🐛 Describe the bug model infer bash : vllm serve /workspace/models/DeepSeek-V2-Lite-Chat \ --gpu-memory-utilization 0.80 \ --max-model-len 8000 \ --max-num-batched-tokens 32000 \ --max-num-seqs 1024 \ --trust-remote-code \ > deepseek-v2_triton$(date +%Y%m%d-%H%M).log & conda env package list: Package Version --------------------------------- --------------------------------------- aiohappyeyeballs 2.4.8 aiohttp 3.11.13 aiosignal 1.3.2 airportsdata 20250224 annotated-types 0.7.0 anyio 4.8.0 astor 0.8.1 async-timeout 5.0.1 attrs 25.1.0 blake3 1.0.4 certifi 2025.1.31 charset-normalizer 3.4.1 click 8....

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: %H%M).log & conda env package list: Package Version --------------------------------- --------------------------------------- aiohappyeyeballs 2.4.8 aiohttp 3.11.13 aiosignal 1.3.2 airportsdata
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: g ### Your current environment python3 benchmark_serving.py \ --model /workspace/models/DeepSeek-V2-Lite-Chat \ --host 0.0.0.0 \ --port 8001 \ --dataset-name random \ --num-prompts 1000 \ --random-input-len 1000 \ --ran...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: [Bug]: benchmark_serving --profile Never received a valid chunk to calculate TTFT.This response will be marked as failed! bug ### Your current environment python3 benchmark_serving.py \ --model /workspace/models/Deep
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 3.1.1 compressed-tensors 0.9.2 cupy-cuda12x 13.4.0 datasets 3.3.2 depyf 0.18.0 dill 0.3.8 diskcache 5.6.3 distro
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ile parameter take error RequestFuncOutput(generated_text='', success=False, latency=0.0, output_tokens=0, ttft=0.0, itl=[], tpot=0.0, prompt_len=1000, error='Never received a valid chunk to calculate TTFT.This response...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
