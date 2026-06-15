# vllm-project/vllm#29178: [Bug]: Internal: AttributeError: module 'triton.language' has no attribute 'constexpr_function'

| 字段 | 值 |
| --- | --- |
| Issue | [#29178](https://github.com/vllm-project/vllm/issues/29178) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Internal: AttributeError: module 'triton.language' has no attribute 'constexpr_function'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug error: creating server: Invalid argument - load failed for model 'yiyao': version 1 is at UNAVAILABLE state: Internal: AttributeError: module 'triton.language' has no attribute 'constexpr_function' At: /usr/local/lib/python3.12/site-packages/triton_kernels/numerics_details/flexpoint.py(55): (488): _call_with_frames_removed (995): exec_module (950): _load_unlocked (1334): _find_and_load_unlocked (1360): _find_and_load /usr/local/lib/python3.12/site-packages/triton_kernels/matmul_ogs_details/_matmul_ogs.py(8): (488): _call_with_frames_removed (995): exec_module (950): _load_unlocked (1334): _find_and_load_unlocked (1360): _find_and_load /usr/local/lib/python3.12/site-packages/triton_kernels/matmul_ogs.py(15): (488): _call_with_frames_removed (995): exec_module (950): _load_unlocked (1334): _find_and_load_unlocked (1360): _find_and_load /usr/local/lib/python3.12/site-packages/vllm/model_executor/layers/fused_moe/config.py(27): (488): _call_with_frames_removed (995): exec_module (950): _load_unlocked (1334): _find_and_load_unlocked (1360): _find_and_load /usr/local/lib/python3.12/site-packages/vllm/model_executor/layers/fused_moe/__i...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ribe the bug error: creating server: Invalid argument - load failed for model 'yiyao': version 1 is at UNAVAILABLE state: Internal: AttributeError: module 'triton.language' has no attribute 'constexpr_function' At: /usr...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: [Bug]: Internal: AttributeError: module 'triton.language' has no attribute 'constexpr_function' bug;stale ### Your current environment ### 🐛 Describe the bug error: creating server: Invalid argument - load failed for mo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: rror: creating server: Invalid argument - load failed for model 'yiyao': version 1 is at UNAVAILABLE state: Internal: AttributeError: module 'triton.language' has no attribute 'constexpr_function' At: /usr/local/lib/pyt...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: _function' At: /usr/local/lib/python3.12/site-packages/triton_kernels/numerics_details/flexpoint.py(55): (488): _call_with_frames_removed (995): exec_module (950): _load_unlocked (1334): _find_and_load_unlocked (1360):...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: es. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
