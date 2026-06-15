# vllm-project/vllm#28516: [Bug]:  You can only use one kind of structured outputs constraint but multt iple are specified

| 字段 | 值 |
| --- | --- |
| Issue | [#28516](https://github.com/vllm-project/vllm/issues/28516) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  You can only use one kind of structured outputs constraint but multt iple are specified

### Issue 正文摘录

```text ^[[1;36m(EngineCore_DP0 pid=1937638)^[[0;0m ValueError: You can only use one kind of structured outputs constraint but multiple are specc ified: {'json': '{"name":"string", "identityCode":"string", "bankName":"string", "accountName":"string", "accountCode":"string"}', 'regee x': None, 'choice': None, 'grammar': None, 'json_object': True, 'disable_fallback': False, 'disable_any_whitespace': False, 'disable_addd itional_properties': False, 'whitespace_pattern': None, 'structural_tag': None, '_backend': 'xgrammar', '_backend_was_auto': True} ^[[1;36m(EngineCore_DP0 pid=1937638)^[[0;0m ^[[1;36m(EngineCore_DP0 pid=1937638)^[[0;0m The above exception was the direct cause of the following exception: ^[[1;36m(EngineCore_DP0 pid=1937638)^[[0;0m ^[[1;36m(EngineCore_DP0 pid=1937638)^[[0;0m Traceback (most recent call last): ^[[1;36m(EngineCore_DP0 pid=1937638)^[[0;0m File "/root/miniforge3/envs/vllm0110/lib/python3.12/threading.py", line 1075, in _bootstraa p_inner ^[[1;36m(EngineCore_DP0 pid=1937638)^[[0;0m self.run() ^[[1;36m(EngineCore_DP0 pid=1937638)^[[0;0m File "/root/miniforge3/envs/vllm0110/lib/python3.12/threading.py", line 1012, in run ^[[1;36m(EngineCore_DP0 pid=1937638)^[...

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: x': None, 'choice': None, 'grammar': None, 'json_object': True, 'disable_fallback': False, 'disable_any_whitespace': False, 'disable_addd itional_properties': False, 'whitespace_pattern': None, 'structural_tag': None, '...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: in process_input_sockets ^[[1;36m(EngineCore_DP0 pid=1937638)^[[0;0m request = add_request_decoder.decode(data_frames) ^[[1;36m(EngineCore_DP0 pid=1937638)^[[0;0m ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ^[[1;36m(EngineC...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: only use one kind of structured outputs constraint but multt iple are specified bug ```text ^[[1;36m(EngineCore_DP0 pid=1937638)^[[0;0m ValueError: You can only use one kind of structured outputs constraint but multiple...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: oice': None, 'grammar': None, 'json_object': True, 'disable_fallback': False, 'disable_any_whitespace': False, 'disable_addd itional_properties': False, 'whitespace_pattern': None, 'structural_tag': None, '_backend': 'x...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
