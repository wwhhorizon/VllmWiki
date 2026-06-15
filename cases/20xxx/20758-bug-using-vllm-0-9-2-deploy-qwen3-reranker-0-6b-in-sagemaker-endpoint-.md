# vllm-project/vllm#20758: [Bug]: using vllm 0.9.2 deploy Qwen3-Reranker-0.6B in SageMaker Endpoint failed

| 字段 | 值 |
| --- | --- |
| Issue | [#20758](https://github.com/vllm-project/vllm/issues/20758) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: using vllm 0.9.2 deploy Qwen3-Reranker-0.6B in SageMaker Endpoint failed

### Issue 正文摘录

### Your current environment - SageMaker Endpoint ### 🐛 Describe the bug I use the sagemaker-entrypoint.sh to build a customer docker image based on vllm/vllm-openai:v0.9.2 ``` entrypoint.sh #!/bin/bash # Define the prefix for environment variables to look for PREFIX="SM_VLLM_" ARG_PREFIX="--" # Initialize an array for storing the arguments # port 8080 required by sagemaker, https://docs.aws.amazon.com/sagemaker/latest/dg/your-algorithms-inference-code.html#your-algorithms-inference-code-container-response ARGS=(--port 8080) # Loop through all environment variables while IFS='=' read -r key value; do # Remove the prefix from the key, convert to lowercase, and replace underscores with dashes arg_name=$(echo "${key#"${PREFIX}"}" | tr '[:upper:]' '[:lower:]' | tr '_' '-') # Add the argument name and value to the ARGS array ARGS+=("${ARG_PREFIX}${arg_name}") if [ -n "$value" ]; then ARGS+=("$value") fi done < <(env | grep "^${PREFIX}") # echo nvidia-smi info nvidia-smi # Pass the collected arguments to the main entrypoint echo ${ARGS[@]} exec python3 -m vllm.entrypoints.openai.api_server "${ARGS[@]}" ``` Dockerfile ``` FROM vllm/vllm-openai:v0.9.2 COPY . . RUN chmod +x entrypoint.sh E...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Endpoint ### 🐛 Describe the bug I use the sagemaker-entrypoint.sh to build a customer docker image based on vllm/vllm-openai:v0.9.2 ``` entrypoint.sh #!/bin/bash # Define the prefix for environment variables to look for...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: using vllm 0.9.2 deploy Qwen3-Reranker-0.6B in SageMaker Endpoint failed bug ### Your current environment - SageMaker Endpoint ### 🐛 Describe the bug I use the sagemaker-entrypoint.sh to build a customer docker i...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: n/bash # Define the prefix for environment variables to look for PREFIX="SM_VLLM_" ARG_PREFIX="--" # Initialize an array for storing the arguments # port 8080 required by sagemaker, https://docs.aws.amazon.com/sagemaker...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: eceive, sender) File "/usr/local/lib/python3.12/dist-packages/starlette/routing.py", line 714, in __call__ await self.middleware_stack(scope, receive, send) File "/usr/local/lib/python3.12/dist-packages/starlette/routin...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: ayload), ContentType="application/json" ) print(response['Body'].read().decode("utf-8")) ``` error ``` Traceback (most recent call last): File "/usr/local/lib/python3.12/dist-packages/uvicorn/protocols/http/httptools_im...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
