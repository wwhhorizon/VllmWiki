# vllm-project/vllm#23013: [Bug]: tracking, gpt-oss broken on main on blackwell

| 字段 | 值 |
| --- | --- |
| Issue | [#23013](https://github.com/vllm-project/vllm/issues/23013) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;hardware_porting;sampling_logits |
| 子分类 |  |
| Operator 关键词 | cuda;kernel;sampling |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: tracking, gpt-oss broken on main on blackwell

### Issue 正文摘录

### Your current environment From @WoosukKwon Can anyone run gpt-oss on B200? I tried it on the current main 3 times, and failed in 3 different ways The first error I met was on detokenizer (I used LLM api, so the output didn’t go through harmony btw) The second error was cuda illegal memory access Actually, the flashinfer top-p sampling kernel returns an out-of-bound token id: sampler_output.sampled_token_ids: tensor([[986987020]] After disabling flashinfer, I don’t get the errors above, but get gibberish outputs I think this is a known issue on blackwell though ### 🐛 Describe the bug see above ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: tracking, gpt-oss broken on main on blackwell bug ### Your current environment From @WoosukKwon Can anyone run gpt-oss on B200? I tried it on the current main 3 times, and failed in 3 different ways The first err...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ony btw) The second error was cuda illegal memory access Actually, the flashinfer top-p sampling kernel returns an out-of-bound token id: sampler_output.sampled_token_ids: tensor([[986987020]] After disabling flashinfer...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: tracking, gpt-oss broken on main on blackwell bug ### Your current environment From @WoosukKwon Can anyone run gpt-oss on B200? I tried it on the current main 3 times, and failed in 3 different ways The first err...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions. performance frontend_api;hardware_porting;sampling_logits cuda;kernel;sampling Your c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
