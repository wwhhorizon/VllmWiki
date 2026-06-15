# vllm-project/vllm#13259: [Performance]: Added request take too much time, and the model will not run untill all the request are added into the cache

| 字段 | 值 |
| --- | --- |
| Issue | [#13259](https://github.com/vllm-project/vllm/issues/13259) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Performance]: Added request take too much time, and the model will not run untill all the request are added into the cache

### Issue 正文摘录

### Proposal to improve performance ``` INFO 02-14 11:57:32 engine.py:275] Added request chatcmpl-1af15bd86d5f413683cd727e1028852c. INFO 02-14 11:57:32 engine.py:275] Added request chatcmpl-b4e5eba8d8d144a0813ffb6e378ee784. INFO 02-14 11:57:32 engine.py:275] Added request chatcmpl-1ca0f490ea104efc9884777815e51618. INFO 02-14 11:57:33 engine.py:275] Added request chatcmpl-984040d9c3cf424984a719970de484f5. INFO 02-14 11:57:33 engine.py:275] Added request chatcmpl-532cbdba66794d859a61423270e06baf. INFO 02-14 11:57:33 engine.py:275] Added request chatcmpl-083f1271382f4bd189c35a604b137bc8. INFO 02-14 11:57:33 engine.py:275] Added request chatcmpl-d5c44ff025cc44149c4b64dcd30fa494. INFO 02-14 11:57:34 engine.py:275] Added request chatcmpl-087039221d0a463a9779b4f072b853ee. INFO 02-14 11:57:34 engine.py:275] Added request chatcmpl-22734de905b74010910ea9511d27462c. INFO 02-14 11:57:34 engine.py:275] Added request chatcmpl-3ad72c9c11f84b49ac6ae2437e1064cc. INFO 02-14 11:57:35 engine.py:275] Added request chatcmpl-180206440e054294b53baf79ffbedce7. INFO 02-14 11:57:35 engine.py:275] Added request chatcmpl-68d902705e3743a0b72add7e2711f9a0. INFO 02-14 11:57:35 engine.py:275] Added request chatcm...

## 候选优化模式

- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: st will wait until the 100th request is cached. How can I reduce the the latency and maximum the GPU usage? ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your cu...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Performance]: Added request take too much time, and the model will not run untill all the request are added into the cache performance;stale ### Proposal to improve performance ``` INFO 02-14 11:57:32 engine.py:275] Ad...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Performance]: Added request take too much time, and the model will not run untill all the request are added into the cache performance;stale ### Proposal to improve performance ``` INFO 02-14 11:57:32 engine.py:275] Ad...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
