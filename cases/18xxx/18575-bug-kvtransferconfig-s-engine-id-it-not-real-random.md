# vllm-project/vllm#18575: [Bug]: KVTransferConfig's engine_id it not real random

| 字段 | 值 |
| --- | --- |
| Issue | [#18575](https://github.com/vllm-project/vllm/issues/18575) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: KVTransferConfig's engine_id it not real random

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ``` from dataclasses import dataclass import uuid @dataclass class Foo: id: str = str(uuid.uuid4()) if __name__ == "__main__": for _ in range(2): foo = Foo() print(foo.id) for _ in range(2): print(str(uuid.uuid4())) ``` or https://github.com/vllm-project/vllm/commit/b5880c9bd5ff23ac90cb9ac0eb91bd7d5eadf952 We decorate `KVTransferConfig` with `dataclass` and provide `engine_id: str(uuid.uuid4())`, this means if we create the config multiple times, the `engine_id` is actually identical. See above reproduction script. This could be pitfall if people generate the config in a central place and launch multiple servers, like https://github.com/ray-project/ray/pull/53092 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: our current environment ### 🐛 Describe the bug ``` from dataclasses import dataclass import uuid @dataclass class Foo: id: str = str(uuid.uuid4()) if __name__ == "__main__": for _ in range(2): foo = Foo() print(foo.id)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 092 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: KVTransferConfig's engine_id it not real random bug ### Your current environment ### 🐛 Describe the bug ``` from dataclasses import dataclass import uuid @dataclass class Foo: id: str = str(uuid.uuid4()) if __nam...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
