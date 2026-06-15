# vllm-project/vllm#18420: [RFC]: Support prefix and postfix addition to JSON and JSON schema for structured outputs

| 字段 | 值 |
| --- | --- |
| Issue | [#18420](https://github.com/vllm-project/vllm/issues/18420) |
| 状态 | closed |
| 标签 | RFC;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [RFC]: Support prefix and postfix addition to JSON and JSON schema for structured outputs

### Issue 正文摘录

### Motivation. [Command A](https://huggingface.co/CohereLabs/c4ai-command-a-03-2025) by cohere have specific prefixes and postfixes such as and which are generated at the start and end of responses. The current guided decoding interface do not have support for prefixes and suffixes that can be added specifically to JSON and JSON Schema. An example output generation would be as follows : ``` { "scoreboard": [ { "player_name": "Player1", "score": 12500, "level": 10, "achievements": ["Speedster", "Master of Coins"] }, { "player_name": "Pro Gamer", "score": 15200, "level": 15, "achievements": ["High Score", "Level Up Expert"] }, { "player_name": "Game Guru", "score": 9800, "level": 8, "achievements": ["Newbie", "Coin Collector"] }, { "player_name": "Ace Player", "score": 13500, "level": 12, "achievements": ["Speed Master", "Level Up Hero"] }, { "player_name": "Super Star", "score": 11000, "level": 9, "achievements": ["Speedster", "Level Up Ace"] } ] } ``` ### Proposed Change. Proposed Change. : With the inclusion of `structural_tag `in 0.8.5, we can use the being and end tags as and respectively and set the trigger string to be ` `, this would ensure that is generating in the non gui...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: s://huggingface.co/CohereLabs/c4ai-command-a-03-2025) by cohere have specific prefixes and postfixes such as and which are generated at the start and end of responses. The current guided decoding interface do not have s...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: ma for structured outputs RFC;stale ### Motivation. [Command A](https://huggingface.co/CohereLabs/c4ai-command-a-03-2025) by cohere have specific prefixes and postfixes such as and which are generated at the start and e...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: 15200, "level": 15, "achievements": ["High Score", "Level Up Expert"] }, { "player_name": "Game Guru", "score": 9800, "level": 8, "achievements": ["Newbie", "Coin Collector"] }, { "player_name": "Ace Player", "score": 1...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: and postfix addition to JSON and JSON schema for structured outputs RFC;stale ### Motivation. [Command A](https://huggingface.co/CohereLabs/c4ai-command-a-03-2025) by cohere have specific prefixes and postfixes such as...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
