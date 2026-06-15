# vllm-project/vllm#22361: [Bug]: gpt-oss-120b does not support hybrid data parallel and tensor parallel

| 字段 | 值 |
| --- | --- |
| Issue | [#22361](https://github.com/vllm-project/vllm/issues/22361) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: gpt-oss-120b does not support hybrid data parallel and tensor parallel

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug Currently `vllm serve` does not support hybrid tensor (expert) parallel and data parallel. When I set `tp=1` and enable expert parallel: ``` set -x export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 pip install --ignore-requires-python --pre /mnt/hdfs/jiaofangkai/others/vllm-0.10.1+gptoss-cp38-abi3-linux_x86_64.whl \ --extra-index-url https://wheels.vllm.ai/gpt-oss/ \ --extra-index-url https://download.pytorch.org/whl/nightly/cu128 pip install --force-reinstall --no-cache-dir numpy==2.2 pandas pip install --upgrade openai #export VLLM_HOST_IP=$(hostname -I | awk '{print $1}') #export HOST_IP=$(hostname -I | awk '{print $1}') IFS=',' read -ra HOSTS &2 exit 1 fi dp_address="tcp://[${ip}]:${port}" # [1;36m(APIServer pid=138855)[0;0m sys.exit(main()) [1;36m(APIServer pid=138855)[0;0m ^^^^^^ [1;36m(APIServer pid=138855)[0;0m File "/home/tiger/.local/lib/python3.11/site-packages/vllm/entrypoints/cli/main.py", line 54, in main [1;36m(APIServer pid=138855)[0;0m args.dispatch_function(args) [1;36m(APIServer pid=138855)[0;0m File "/home/tiger/.local/lib/python3.11/site-packages/vllm/entrypoints/cli/serve.py", line 50, in cmd [1;36m(APIServe...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: expert parallel: ``` set -x export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 pip install --ignore-requires-python --pre /mnt/hdfs/jiaofangkai/others/vllm-0.10.1+gptoss-cp38-abi3-linux_x86_64.whl \ --extra-index-url https://wheels...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: gpt-oss-120b does not support hybrid data parallel and tensor parallel bug;stale ### Your current environment ### 🐛 Describe the bug Currently `vllm serve` does not support hybrid tensor (expert) parallel and dat...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: /main.py", line 54, in main [1;36m(APIServer pid=138855)[0;0m args.dispatch_function(args) [1;36m(APIServer pid=138855)[0;0m File "/home/tiger/.local/lib/python3.11/site-packages/vllm/entrypoints/cli/serve.py", line...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: * 2 ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: Describe the bug Currently `vllm serve` does not support hybrid tensor (expert) parallel and data parallel. When I set `tp=1` and enable expert parallel: ``` set -x export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1 pip install --i...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
