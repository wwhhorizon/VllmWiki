# vllm-project/vllm#17702: [Feature]: The v1 engine does not support `add_logger`.

| 字段 | 值 |
| --- | --- |
| Issue | [#17702](https://github.com/vllm-project/vllm/issues/17702) |
| 状态 | closed |
| 标签 | feature request;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Feature]: The v1 engine does not support `add_logger`.

### Issue 正文摘录

### 🚀 The feature, motivation and pitch When I tried to add Prometheus metric monitoring with the following code： ```python from vllm.entrypoints.logger import RequestLogger from vllm.engine.metrics import RayPrometheusStatLogger self.engine = AsyncLLMEngine.from_engine_args(engine_args) vllm_config = self.engine_args.create_engine_config(UsageContext.ENGINE_CONTEXT) additional_metrics_logger: RayPrometheusStatLogger = RayPrometheusStatLogger( local_interval=0.5, labels=dict(model_name=self.config["model_name"],instance_name = self.config["log_instance_name"]), vllm_config=vllm_config ) self.engine.add_logger("ray", additional_metrics_logger) ``` The following error occurs： ``` shell (ServeController pid=14828) File "/home/ray/anaconda3/lib/python3.11/concurrent/futures/_base.py", line 449, in result (ServeController pid=14828) return self.__get_result() (ServeController pid=14828) ^^^^^^^^^^^^^^^^^^^ (ServeController pid=14828) File "/home/ray/anaconda3/lib/python3.11/concurrent/futures/_base.py", line 401, in __get_result (ServeController pid=14828) raise self._exception (ServeController pid=14828) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ (ServeController pid=14828) File "/home/ray...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: Logger self.engine = AsyncLLMEngine.from_engine_args(engine_args) vllm_config = self.engine_args.create_engine_config(UsageContext.ENGINE_CONTEXT) additional_metrics_logger: RayPrometheusStatLogger = RayPrometheusStatLo...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: itoring with the following code： ```python from vllm.entrypoints.logger import RequestLogger from vllm.engine.metrics import RayPrometheusStatLogger self.engine = AsyncLLMEngine.from_engine_args(engine_args) vllm_config...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Feature]: The v1 engine does not support `add_logger`. feature request;stale ### 🚀 The feature, motivation and pitch When I tried to add Prometheus metric monitoring with the following code： ```python from vllm.entrypo...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: se_ ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: packages/ray/serve/_private/replica.py", line 965, in initialize_and_get_metadata (ServeController pid=14828) await self._replica_impl.initialize(deployment_config) (ServeController pid=14828) File "/home/ray/anaconda3/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
