# vllm-project/vllm#35563: [Bug]: Subset of Lora unit tests fail on NVIDIA VLLM Stack

| 字段 | 值 |
| --- | --- |
| Issue | [#35563](https://github.com/vllm-project/vllm/issues/35563) |
| 状态 | open |
| 标签 | bug;stale |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Subset of Lora unit tests fail on NVIDIA VLLM Stack

### Issue 正文摘录

### Your current environment Repro: Latest NVIDIA VLLM Docker container from: https://catalog.ngc.nvidia.com/orgs/nvidia/containers/vllm/tags?version=26.02-py3 ``` cp $(python3 -c "import vllm, os; print(os.path.dirname(vllm.__file__))")/*.abi3.so /opt/vllm/vllm-src/vllm/ 2>/dev/null mkdir -p /opt/vllm/vllm-src/vllm/vllm_flash_attn cp -r /usr/local/lib/python3.12/dist-packages/vllm/vllm_flash_attn/* /opt/vllm/vllm-src/vllm/vllm_flash_attn/ pip install -q tblib librosa cd /opt/vllm/vllm-src py.test -s tests/lora -v --junitxml=/logs/lora.xml ``` Issues observed with: test_qwen3moe_tp, test_qwenvl, test_default_mm_loras, test_llama_tp, test_minicpmv_tp, test_mixtral, test_punica_ops, test_transformers_model Log attached: [lora-logs.txt.zip](https://github.com/user-attachments/files/25617456/lora-logs.txt.zip) ### 🐛 Describe the bug The logs and test failures are above. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Stack bug;stale ### Your current environment Repro: Latest NVIDIA VLLM Docker container from: https://catalog.ngc.nvidia.com/orgs/nvidia/containers/vllm/tags?version=26.02-py3 ``` cp $(python3 -c "import vllm, os; print...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: s tests/lora -v --junitxml=/logs/lora.xml ``` Issues observed with: test_qwen3moe_tp, test_qwenvl, test_default_mm_loras, test_llama_tp, test_minicpmv_tp, test_mixtral, test_punica_ops, test_transformers_model Log attac...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ve. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: ts/lora -v --junitxml=/logs/lora.xml ``` Issues observed with: test_qwen3moe_tp, test_qwenvl, test_default_mm_loras, test_llama_tp, test_minicpmv_tp, test_mixtral, test_punica_ops, test_transformers_model Log attached:...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: Subset of Lora unit tests fail on NVIDIA VLLM Stack bug;stale ### Your current environment Repro: Latest NVIDIA VLLM Docker container from: https://catalog.ngc.nvidia.com/orgs/nvidia/containers/vllm/tags?version=...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
