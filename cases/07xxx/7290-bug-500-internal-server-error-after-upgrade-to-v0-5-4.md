# vllm-project/vllm#7290: [Bug]: "500 Internal Server Error" after upgrade to v0.5.4

| 字段 | 值 |
| --- | --- |
| Issue | [#7290](https://github.com/vllm-project/vllm/issues/7290) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 13; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | distributed_parallel;frontend_api;model_support;quantization |
| 子分类 |  |
| Operator 关键词 | quantization |
| 症状 | crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: "500 Internal Server Error" after upgrade to v0.5.4

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug After I upgraded to v0.5.4, got "500 Internal Server Error". My manifest snippet to start vllm: ```yaml containers: - name: 8x7b-open image: vllm/vllm-openai:v0.5.4 command: ["python3", "-m", "vllm.entrypoints.openai.api_server"] args: ["--model", "hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4", "--host", "0.0.0.0", "--port", "8080", "--tensor-parallel-size", "2", "--seed", "42", "--trust-remote-code"] securityContext: privileged: true ports: - containerPort: 8080 env: - name: OMP_NUM_THREADS value: "2" volumeMounts: - mountPath: "/root/.cache" name: ceph-volume resources: limits: cpu: '12' memory: 200Gi nvidia.com/gpu: '2' requests: cpu: '12' memory: 200Gi nvidia.com/gpu: '2' ``` Backtrace log: ``` INFO: 10.254.17.246:59936 - "POST /v1/chat/completions HTTP/1.1" 500 Internal Server Error ERROR: Exception in ASGI application Traceback (most recent call last): File "/usr/local/lib/python3.10/dist-packages/uvicorn/protocols/http/httptools_impl.py", line 399, in run_asgi result = await app( # type: ignore[func-returns-value] File "/usr/local/lib/python3.10/dist-packages/uvicorn...

## 现有链接修复摘要

#7394 [Bugfix][Frontend] Fix Issues Under High Load With `zeromq` Frontend

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: args: ["--model", "hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4", "--host", "0.0.0.0", "--port", "8080", "--tensor-parallel-size", "2", "--seed", "42", "--trust-remote-code"] securityContext:
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ceive, sender) File "/usr/local/lib/python3.10/dist-packages/starlette/routing.py", line 756, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.10/dist-packages/starlette/routing...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: args: ["--model", "hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4", "--host", "0.0.0.0", "--port", "8080", "--tensor-parallel-size", "2", "--seed", "42", "--trust-remote-code"] securityContext:
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: "500 Internal Server Error" after upgrade to v0.5.4 bug;stale ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug After I upgraded to v0.5.4, got "500 Internal Se...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: lel;frontend_api;model_support;quantization quantization crash dtype;env_dependency #7394 [Bugfix][Frontend] Fix Issues Under High Load With `zeromq` Frontend Your current environment

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#7394](https://github.com/vllm-project/vllm/pull/7394) | closes_keyword | 0.95 | [Bugfix][Frontend] Fix Issues Under High Load With `zeromq` Frontend | FIX - #7309 - #7290 ### UPDATE 8/20 POST OFFLINE DISCUSSION Per discussion offline with @njhill @simon-mo and @youkaichao After much further investigation, we ran int |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
