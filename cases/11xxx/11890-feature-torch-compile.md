# vllm-project/vllm#11890: [feature]: torch compile 

| 字段 | 值 |
| --- | --- |
| Issue | [#11890](https://github.com/vllm-project/vllm/issues/11890) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [feature]: torch compile 

### Issue 正文摘录

### Your current environment vllm 0.6.5 ### How would you like to use vllm in vllm/compilation/wrapper.py def bytecode_hook(self, old_code: CodeType, new_code: CodeType): """Hook to save the compiled bytecode for direct execution.""" if old_code is not self.original_code_object: return when old_code is not self.original_code_object happened? i using vllm torch compilation impl in ourself framework, but when i use not fullgraph, i get this return when graph break, then trigger this assert assert not self._called, "VllmBackend can only be called once" so can support compile when graph break？ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: when graph break, then trigger this assert assert not self._called, "VllmBackend can only be called once" so can support compile when graph break？ ### Before submitting a new issue... - [X] Make sure you already searche...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: [feature]: torch compile usage ### Your current environment vllm 0.6.5 ### How would you like to use vllm in vllm/compilation/wrapper.py def bytecode_hook(self, old_code: CodeType, new_code: CodeType): """Hook to save t...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ak？ ### Before submitting a new issue... - [X] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
