# vllm-project/vllm#28598: [Bug] [ROCm] [AITER]: AITER MHA accuracy degrades after PR #25763

| 字段 | 值 |
| --- | --- |
| Issue | [#28598](https://github.com/vllm-project/vllm/issues/28598) |
| 状态 | closed |
| 标签 | bug;rocm |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug] [ROCm] [AITER]: AITER MHA accuracy degrades after PR #25763

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug @sarckk has reported that after this PR https://github.com/vllm-project/vllm/pull/25763 There are some accuracy issues. @sarckk has drilled down to the plausible cause at https://github.com/ROCm/aiter/issues/1368 . `docker pull rocm/vllm-dev:nightly` (11 Nov 2025) it is using AITER version specified in https://github.com/vllm-project/vllm/blob/3eb0c2673e128714073f7e3fd105cf962a4c8c16/docker/Dockerfile.rocm_base#L10 ``` #!/bin/bash rm -rf /root/.cache/vllm/ echo "Qwen/Qwen3-32B" export VLLM_RPC_TIMEOUT=1800000 export SAFETENSORS_FAST_GPU=1 export MODEL_PATH=Qwen/Qwen3-32B VLLM_ROCM_USE_AITER=1 \ vllm serve $MODEL_PATH \ -tp 2 \ --trust-remote-code \ --disable-log-requests ``` lm_eval command ```bash #!/bin/bash lm_eval \ --model local-completions \ --tasks gsm8k \ --model_args model=Qwen/Qwen3-32B,base_url=http://127.0.0.1:8000/v1/completions \ --batch_size 100 ``` ## Accuracy `gsm8k` Model `Qwen/Qwen3-32B` |Metric | No AITER (Baseline) | AITER (in Dockerfile, older commit) | new AITER commit from main branch | |-------|----------------------| ----------------------------| -----------------------------------------| | flexible-extr...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: to the plausible cause at https://github.com/ROCm/aiter/issues/1368 . `docker pull rocm/vllm-dev:nightly` (11 Nov 2025) it is using AITER version specified in https://github.com/vllm-project/vllm/blob/3eb0c2673e12871407...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug] [ROCm] [AITER]: AITER MHA accuracy degrades after PR #25763 bug;rocm ### Your current environment ### 🐛 Describe the bug @sarckk has reported that after this PR https://github.com/vllm-project/vllm/pull/25763 Ther...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: [Bug] [ROCm] [AITER]: AITER MHA accuracy degrades after PR #25763 bug;rocm ### Your current environment ### 🐛 Describe the bug @sarckk has reported that after this PR https://github.com/vllm-project/vllm/pull/25763 Ther...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ockerfile.rocm_base#L10 ``` #!/bin/bash rm -rf /root/.cache/vllm/ echo "Qwen/Qwen3-32B" export VLLM_RPC_TIMEOUT=1800000 export SAFETENSORS_FAST_GPU=1 export MODEL_PATH=Qwen/Qwen3-32B VLLM_ROCM_USE_AITER=1 \ vllm serve $...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug] [ROCm] [AITER]: AITER MHA accuracy degrades after PR #25763 bug;rocm ### Your current environment ### 🐛 Describe the bug @sarckk has reported that after this PR https://github.com/vllm-project/vllm/pull/25763 Ther...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
