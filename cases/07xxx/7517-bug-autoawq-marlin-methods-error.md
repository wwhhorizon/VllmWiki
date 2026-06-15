# vllm-project/vllm#7517: [Bug]:  AutoAWQ marlin methods error

| 字段 | 值 |
| --- | --- |
| Issue | [#7517](https://github.com/vllm-project/vllm/issues/7517) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  AutoAWQ marlin methods error

### Issue 正文摘录

### Your current environment vllm 0.5.4 ### 🐛 Describe the bug autoawq marlin must with no zero point， but vllm： ```python def query_marlin_supported_quant_types(has_zp: bool, min_capability: Optional[int] = None): if min_capability is None: major, minor = current_platform.get_device_capability() min_capability = major * 10 + minor if min_capability < 80: return [] if has_zp: # AWQ style, unsigned + runtime zero-point return [scalar_types.uint4, scalar_types.uint8] else: # GPTQ style, unsigned + symmetric bias # TODO: once fp8_marlin is merged into "gptq_marlin" we should be able # to add `scalar_types.float8_e4m3fn` here return [scalar_types.uint4b8, scalar_types.uint8b128]` ``` this would error### ###

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: must with no zero point， but vllm： ```python def query_marlin_supported_quant_types(has_zp: bool, min_capability: Optional[int] = None): if min_capability is None: major, minor = current_platform.get_device_capability()...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ted_quant_types(has_zp: bool, min_capability: Optional[int] = None): if min_capability is None: major, minor = current_platform.get_device_capability() min_capability = major * 10 + minor if min_capability < 80: return...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: zero-point return [scalar_types.uint4, scalar_types.uint8] else: # GPTQ style, unsigned + symmetric bias # TODO: once fp8_marlin is merged into "gptq_marlin" we should be able # to add `scalar_types.float8_e4m3fn` here...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: [Bug]: AutoAWQ marlin methods error bug;stale ### Your current environment vllm 0.5.4 ### 🐛 Describe the bug autoawq marlin must with no zero point， but vllm： ```python def query_marlin_supported_quant_types(has_zp: boo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
