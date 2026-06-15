# vllm-project/vllm#706: Same generate params but got totally different result

| 字段 | 值 |
| --- | --- |
| Issue | [#706](https://github.com/vllm-project/vllm/issues/706) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> Same generate params but got totally different result

### Issue 正文摘录

Hi, I have a params with do_sample False, the result on huggingface are pretty good. But same set in vllm, the model likes a stupid bird. ``` sampling_params = SamplingParams( temperature=generating_args.temperature, top_p=generating_args.top_p, max_tokens=800, frequency_penalty=generating_args.repetition_penalty, use_beam_search=False, ignore_eos=False, ) ``` Please let me know how to resolve the bias? same args: ``` do_sample: Optional[bool] = field(default=True) temperature: Optional[float] = field( default=0.84, metadata={"help": "The value used to modulate the next token probabilities."}, ) top_p: Optional[float] = field( default=0.6, metadata={ "help": "The smallest set of most probable tokens with probabilities that add up to top_p or higher are kept." }, ) top_k: Optional[int] = field(default=40) num_beams: Optional[int] = field(default=1) max_new_tokens: Optional[int] = field(default=800) repetition_penalty: Optional[float] = field(default=1.09) ``` Both set do_sample False. but the result are out of my scope, they are totally different.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: frequency_penalty=generating_args.repetition_penalty, use_beam_search=False, ignore_eos=False, ) ``` Please let me know how to resolve the bias? same args: ``` do_sample: Optional[bool] = field(default=True) temperature...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: ms but got totally different result Hi, I have a params with do_sample False, the result on huggingface are pretty good. But same set in vllm, the model likes a stupid bird. ``` sampling_params = SamplingParams( tempera...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: different result Hi, I have a params with do_sample False, the result on huggingface are pretty good. But same set in vllm, the model likes a stupid bird. ``` sampling_params = SamplingParams( temperature=generating_arg...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
