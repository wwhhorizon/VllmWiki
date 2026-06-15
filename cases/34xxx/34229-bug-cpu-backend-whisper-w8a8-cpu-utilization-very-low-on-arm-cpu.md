# vllm-project/vllm#34229: [Bug]: [CPU Backend] Whisper W8A8 CPU utilization very low on Arm CPU

| 字段 | 值 |
| --- | --- |
| Issue | [#34229](https://github.com/vllm-project/vllm/issues/34229) |
| 状态 | closed |
| 标签 | bug;cpu |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [CPU Backend] Whisper W8A8 CPU utilization very low on Arm CPU

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I ran [W8A8 Whisper](https://huggingface.co/RedHatAI/whisper-large-v3-quantized.w8a8) on 64 Neoverse V1 cores with a high enough batch size, and noticed that the CPU utilization is as follows: * CPU 0: 100% - very utilized! * CPU 0-53: 14% - very under utilized * CPU 54-63: 0% - not utilized at all, it's as if these cores do not exist. Further observations: * This does not happen when `VLLM_CPU_OMP_THREADS_BIND=nobind` - which is not the default case * This does not happen when `VLLM_CPU_OMP_THREADS_BIND=0-53` - i.e. it only happens when you bind to > 54 cores * This does not happen at all for BF16 whisper, w4a8int whisper, w8a8 llama 3.1 8b **What's happening?** - Initially we'll bind threads to cores [here](https://github.com/vllm-project/vllm/blob/main/csrc/cpu/utils.cpp#L25), if you run this script right after this step with the PID logged by the binding step: ``` find "/proc/$PID/task" -maxdepth 2 -name status -print0 2>/dev/null | while IFS= read -r -d '' s; do tid=$(basename "$(dirname "$s")") cpus=$(awk -F'\t' '/^Cpus_allowed_list:/{print $2}' "$s") printf "%s\t%s\n" "$tid" "$cpus" done | sort -k2,2V | head -200 ``` you'l...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 7: g I ran [W8A8 Whisper](https://huggingface.co/RedHatAI/whisper-large-v3-quantized.w8a8) on 64 Neoverse V1 cores with a high enough batch size, and noticed that the CPU utilization is as follows: * CPU 0: 100% - very uti...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: ent environment ### 🐛 Describe the bug I ran [W8A8 Whisper](https://huggingface.co/RedHatAI/whisper-large-v3-quantized.w8a8) on 64 Neoverse V1 cores with a high enough batch size, and noticed that the CPU utilization is...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: t_dtype: torch.dtype = torch.bfloat16, device: str = "cpu", ): # Test for a oneDNN kernel with per-tensor / per-token activation # quantization and per-tensor / per-output channel weight quantization. a = to_int8(torch....
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: [Bug]: [CPU Backend] Whisper W8A8 CPU utilization very low on Arm CPU bug;cpu ### Your current environment ### 🐛 Describe the bug I ran [W8A8 Whisper](https://huggingface.co/RedHatAI/whisper-large-v3-quantized.w8a8) on...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: e that the size of the team is # SPDX-License-Identifier: BSD-3-Clause import sys import sys import torch from vllm import _custom_ops as ops import time def to_int8(tensor: torch.Tensor): return torch.round(tensor.clam...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
