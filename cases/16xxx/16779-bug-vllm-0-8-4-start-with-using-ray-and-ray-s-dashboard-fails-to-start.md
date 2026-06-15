# vllm-project/vllm#16779: [Bug]: vllm 0.8.4 start with using ray, and ray's dashboard fails to start

| 字段 | 值 |
| --- | --- |
| Issue | [#16779](https://github.com/vllm-project/vllm/issues/16779) |
| 状态 | closed |
| 标签 | bug;ray;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm 0.8.4 start with using ray, and ray's dashboard fails to start

### Issue 正文摘录

### Your current environment ```text 2025-04-17 02:50:51,101 INFO utils.py:313 -- Get all modules by type: DashboardHeadModule 2025-04-17 02:50:51,178 INFO utils.py:324 -- Module ray.dashboard.modules.actor.actor_head cannot be loaded because we cannot import all dependencies. Install this module using `pip install 'ray[default]'` for the full dashboard functionality. Error: No module named 'aiohttp_cors' 2025-04-17 02:50:51,211 INFO utils.py:324 -- Module ray.dashboard.modules.data.data_head cannot be loaded because we cannot import all dependencies. Install this module using `pip install 'ray[default]'` for the full dashboard functionality. Error: No module named 'aiohttp_cors' 2025-04-17 02:50:51,233 INFO utils.py:324 -- Module ray.dashboard.modules.event.event_head cannot be loaded because we cannot import all dependencies. Install this module using `pip install 'ray[default]'` for the full dashboard functionality. Error: No module named 'aiohttp_cors' 2025-04-17 02:50:51,235 INFO utils.py:324 -- Module ray.dashboard.modules.healthz.healthz_agent cannot be loaded because we cannot import all dependencies. Install this module using `pip install 'ray[default]'` for the full dash...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ay.dashboard.modules.actor.actor_head cannot be loaded because we cannot import all dependencies. Install this module using `pip install 'ray[default]'` for the full dashboard functionality. Error: No module named 'aioh...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: al. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: m 0.8.4 start with using ray, and ray's dashboard fails to start bug;ray;stale ### Your current environment ```text 2025-04-17 02:50:51,101 INFO utils.py:313 -- Get all modules by type: DashboardHeadModule 2025-04-17 02...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
