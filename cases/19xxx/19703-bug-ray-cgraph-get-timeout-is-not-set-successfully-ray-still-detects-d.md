# vllm-project/vllm#19703: [Bug]: RAY_CGRAPH_get_timeout is not set successfully.  Ray still detects default timeout value.

| 字段 | 值 |
| --- | --- |
| Issue | [#19703](https://github.com/vllm-project/vllm/issues/19703) |
| 状态 | closed |
| 标签 | bug;ray |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: RAY_CGRAPH_get_timeout is not set successfully.  Ray still detects default timeout value.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug # Background I am trying to run multi-node on GB200. I first encountered an error when setting up Ray for the server and that was because CuPy did not support aarch64 so I installed CuPy on the cupy main branch to get around the issue. Reference: https://github.com/ray-project/ray/issues/53128 # Issue Now I am hitting another Ray error when running the server: ```text INFO 06-12 10:46:22 [ray_distributed_executor.py:579] RAY_CGRAPH_get_timeout is set to 300 ERROR 06-12 10:46:34 [core.py:517] EngineCore encountered a fatal error. ERROR 06-12 10:46:34 [core.py:517] Traceback (most recent call last): ERROR 06-12 10:46:34 [core.py:517] File "/usr/local/lib/python3.12/dist-packages/ray/dag/compiled_dag_node.py", line 2515, in _execute_until ERROR 06-12 10:46:34 [core.py:517] result = self._dag_output_fetcher.read(timeout) ERROR 06-12 10:46:34 [core.py:517] ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ERROR 06-12 10:46:34 [core.py:517] File "/usr/local/lib/python3.12/dist-packages/ray/experimental/channel/common.py", line 309, in read ERROR 06-12 10:46:34 [core.py:517] outputs = self._read_list(timeout) ERROR 06-12 10:46:34 [core.py:517] ^^^...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ay for the server and that was because CuPy did not support aarch64 so I installed CuPy on the cupy main branch to get around the issue. Reference: https://github.com/ray-project/ray/issues/53128 # Issue Now I am hittin...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ### 🐛 Describe the bug # Background I am trying to run multi-node on GB200. I first encountered an error when setting up Ray for the server and that was because CuPy did not support aarch64 so I installed CuPy on the cu...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: " "* ]]; then IFS=' ' read -ra ADDR 16 ]]; then ip=${ADDR[1]} else ip=${ADDR[0]} fi echo "We detect space in ip! You are using IPV6 address. We split the IPV4 address as $ip" fi port_head=6379 ip_head=$ip:$port_head exp...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: in _process_engine_step ERROR 06-12 10:46:34 [core.py:517] outputs, model_executed = self.step_fn() ERROR 06-12 10:46:34 [core.py:517] ^^^^^^^^^^^^^^ ERROR 06-12 10:46:34 [core.py:517] File "/usr/local/lib/python3.12/di...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: e.py:517] ray.exceptions.RayChannelTimeoutError: System error: Timed out waiting for object available to read. ObjectID: 00fc911a7833d5d08cfd39cf6b6b31a5fbea02990100000002e1f505 ERROR 06-12 10:46:34 [core.py:517] ERROR...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
