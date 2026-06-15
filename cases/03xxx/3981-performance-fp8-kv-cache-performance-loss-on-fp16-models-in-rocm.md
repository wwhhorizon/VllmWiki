# vllm-project/vllm#3981: [Performance]: FP8 KV Cache performance loss on FP16 models in ROCm

| 字段 | 值 |
| --- | --- |
| Issue | [#3981](https://github.com/vllm-project/vllm/issues/3981) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;distributed_parallel;hardware_porting;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cache;fp8;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: FP8 KV Cache performance loss on FP16 models in ROCm

### Issue 正文摘录

### Your current environment [previous upload](https://github.com/vllm-project/vllm/files/14937936/env.txt) ### 🐛 Describe the bug When running this command `python vllm/benchmarks/benchmark_throughput.py --input-len 512 --output-len 256 --tensor-parallel-size 4 --memory-utilization 0.7 --model ` with the following model setups, performance is inconsistent: 7b 16 bit slows to almost half speed Baseline 4916.03 tok/s @ 6.4 requests/s --kv-cache-dtype FP8 drops to 2405.54 tok/s @ 3.13 requests/s Yet 120b 4 bit GPTQ gets slightly faster, but not outside of what my average benchmarks show so I assume it's just variance Baseline 154.30 tok/s @ 0.2 requests/s FP8 181.35 tok/s @ 0.25 requests/s [Here](https://huggingface.co/valine/OpenPirate) is the 7b fp16 model I attempted this with, along with [this](https://huggingface.co/TheBloke/goliath-120b-GPTQ) 120b 4bit GPTQ This is on a 4x AMD Instinct MI100 system with a GPU bridge, applying the fixes in Dockerfile.rocm to update the FA branch, FA arch, and the numpy fix prior to today's PR https://github.com/vllm-project/vllm/pull/3962 It's possible that the decrease is due to the [lack of FP8 hardware on the card](https://www.amd.com/en/pro...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: [Performance]: FP8 KV Cache performance loss on FP16 models in ROCm bug ### Your current environment [previous upload](https://github.com/vllm-project/vllm/files/14937936/env.txt) ### 🐛 Describe the bug When running thi...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: a 4x AMD Instinct MI100 system with a GPU bridge, applying the fixes in Dockerfile.rocm to update the FA branch, FA arch, and the numpy fix prior to today's PR https://github.com/vllm-project/vllm/pull/3962 It's possibl...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Performance]: FP8 KV Cache performance loss on FP16 models in ROCm bug ### Your current environment [previous upload](https://github.com/vllm-project/vllm/files/14937936/env.txt) ### 🐛 Describe the bug When running thi...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: [Performance]: FP8 KV Cache performance loss on FP16 models in ROCm bug ### Your current environment [previous upload](https://github.com/vllm-project/vllm/files/14937936/env.txt) ### 🐛 Describe the bug When running thi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Performance]: FP8 KV Cache performance loss on FP16 models in ROCm bug ### Your current environment [previous upload](https://github.com/vllm-project/vllm/files/14937936/env.txt) ### 🐛 Describe the bug When running thi...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
