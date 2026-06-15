# vllm-project/vllm#32920: [Bug]: disagg_proxy_demo.py: Method logic error in 'remove_instance_endpoint'

| 字段 | 值 |
| --- | --- |
| Issue | [#32920](https://github.com/vllm-project/vllm/issues/32920) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: disagg_proxy_demo.py: Method logic error in 'remove_instance_endpoint'

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Method error: There's a simple but crucial bug in the "disagg_proxy_demo.py: 'remove_instance_endpoint'" method logic where it incorrectly checks and cycles instances. (Though it's in the examples) Original code: ```python def remove_instance_endpoint(self, instance_type, instance): if instance_type == "decode" and instance in self.decode_instances: self.decode_instances.remove(instance) self.decode_cycler = itertools.cycle(self.decode_instances) if instance_type == "prefill" and instance in self.decode_instances: self.prefill_instances.remove(instance) self.prefill_cycler = itertools.cycle(self.decode_instances) ``` Actual behavior: - When removing **prefill** instances, it incorrectly checks against `self.decode_instances` instead of `self.prefill_instances` - When recreating the cycle for prefill instances, it uses `self.decode_instances` instead of `self.prefill_instances` Proposed fix: ```python if instance_type == "prefill" and instance in self.prefill_instances: self.prefill_instances.remove(instance) self.prefill_cycler = itertools.cycle(self.prefill_instances) ``` ### Before submitting a new issue... - [x] Make sure you...

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: instance_endpoint(self, instance_type, instance): if instance_type == "decode" and instance in self.decode_instances: self.decode_instances.remove(instance) self.decode_cycler = itertools.cycle(self.decode_instances) if...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: onment ### 🐛 Describe the bug Method error: There's a simple but crucial bug in the "disagg_proxy_demo.py: 'remove_instance_endpoint'" method logic where it incorrectly checks and cycles instances. (Though it's in the e...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
