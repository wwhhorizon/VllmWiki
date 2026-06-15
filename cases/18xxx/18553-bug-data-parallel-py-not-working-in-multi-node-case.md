# vllm-project/vllm#18553: [Bug]: data_parallel.py not working in multi-node case

| 字段 | 值 |
| --- | --- |
| Issue | [#18553](https://github.com/vllm-project/vllm/issues/18553) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 16; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: data_parallel.py not working in multi-node case

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug We basically run the data_parallel.py by ```sh python3 data_parallel.py \ --model="path/to/weight" \ --enforce-eager \ --dp-size=2 \ --tp-size=2 \ --node-size=2 \ --node-rank=0 \ --master-addr=${addr} \ --master-port=13345 ``` and the output are as follows: After some debugging, we found that PR #15977 may have introduced this bug by adding the following code: ```python engine = next( (e for e in self.core_engines if e.identity == eng_identity), None) ``` Here, `e.identity` is derived from `local_dp_rank` in data_parallel.py (which should be `b'\x00\x00` in both the master and worker nodes), while `eng_identity` comes from `dp_rank` (which will be `b'\x00\x01` on the worker node). We are working on fixing this. Is this issue already being addressed? Please let us know, thank you. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash env_dependency Your curre...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ou. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rallel;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: y run the data_parallel.py by ```sh python3 data_parallel.py \ --model="path/to/weight" \ --enforce-eager \ --dp-size=2 \ --tp-size=2 \ --node-size=2 \ --node-rank=0 \ --master-addr=${addr} \ --master-port=13345 ``` and...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: development ci_build;distributed_parallel;hardware_porting;model_support;speculative_decoding cuda;operator;triton build_error;crash env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
