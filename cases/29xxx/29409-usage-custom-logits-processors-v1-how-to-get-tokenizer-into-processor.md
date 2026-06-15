# vllm-project/vllm#29409: [Usage]: Custom Logits Processors V1 how to get tokenizer into processor

| 字段 | 值 |
| --- | --- |
| Issue | [#29409](https://github.com/vllm-project/vllm/issues/29409) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: Custom Logits Processors V1 how to get tokenizer into processor

### Issue 正文摘录

### Problem with tokenizer For the second day now, I've been unable to figure out how to get a tokenizer inside a custom processor. I used the processor from the documentation as an example. I examined each object through debug, but couldn't find where to extract the tokenizer. In v0, this was done simply at the request level, by passing an argument to the object. How to pass a tokenizer to the processor? ```python import torch from vllm.config import VllmConfig from vllm.sampling_params import SamplingParams from vllm.v1.sample.logits_processor import (BatchUpdate, LogitsProcessor, MoveDirectionality) class DummyLogitsProcessor(LogitsProcessor): """Fake logit processor to support unit testing and examples""" @classmethod def validate_params(cls, params: SamplingParams): target_token: int | None = params.extra_args and params.extra_args.get( "target_token" ) if target_token is not None and not isinstance(target_token, int): raise ValueError(f"target_token value {target_token} is not int") def __init__(self, vllm_config: "VllmConfig", device: torch.device, is_pin_memory: bool): self.req_info: dict[int, int] = {} def is_argmax_invariant(self) -> bool: """Never impacts greedy samplin...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ""Fake logit processor to support unit testing and examples""" @classmethod def validate_params(cls, params: SamplingParams): target_token: int | None = params.extra_args and params.extra_args.get( "target_token" ) if t...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ment to the object. How to pass a tokenizer to the processor? ```python import torch from vllm.config import VllmConfig from vllm.sampling_params import SamplingParams from vllm.v1.sample.logits_processor import (BatchU...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: n cols = torch.tensor( list(self.req_info.values()), dtype=torch.long, device=logits.device ) rows = torch.tensor( list(self.req_info.keys()), dtype=torch.long, device=logits.device ) values_to_keep = logits[rows, cols]...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: f) -> bool: """Never impacts greedy sampling""" return False def update_state(self, batch_update: BatchUpdate | None): if not batch_update: return # Process added requests. for index, params, _, _ in batch_update.added:
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: w to pass a tokenizer to the processor? ```python import torch from vllm.config import VllmConfig from vllm.sampling_params import SamplingParams from vllm.v1.sample.logits_processor import (BatchUpdate, LogitsProcessor,

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
