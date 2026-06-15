# vllm-project/vllm#31529: [Bug]: vllm 0.12.0 fail to start Qwen3-VL-30B-A3B-Thinking

| 字段 | 值 |
| --- | --- |
| Issue | [#31529](https://github.com/vllm-project/vllm/issues/31529) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;model_support |
| 子分类 | install |
| Operator 关键词 | cuda;kernel;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: vllm 0.12.0 fail to start Qwen3-VL-30B-A3B-Thinking

### Issue 正文摘录

### Your current environment root@bfbeb5cfa732:/work# pip3 freeze accelerate==1.10.1 aiofile==3.9.0 aiofiles==24.1.0 aiohappyeyeballs==2.6.1 aiohttp==3.12.15 aiosignal==1.4.0 annotated-doc==0.0.4 annotated-types==0.7.0 anthropic==0.71.0 anyio==4.10.0 apache-tvm-ffi==0.1.6 astor==0.8.1 attrs==25.3.0 awscrt==0.27.6 bitsandbytes==0.47.0 blake3==1.0.5 blinker==1.4 boto3==1.40.30 botocore==1.40.30 build==1.3.0 cachetools==6.2.0 caio==0.9.24 cbor2==5.7.0 certifi==2025.8.3 cffi==2.0.0 charset-normalizer==3.4.3 click==8.2.1 cloudpickle==3.1.1 cmake==4.1.0 compressed-tensors==0.12.2 cryptography==3.4.8 cuda-bindings==13.1.1 cuda-pathfinder==1.3.3 cuda-python==13.1.1 cufile-python==0.1.1 cupy-cuda12x==13.6.0 dbus-python==1.2.18 -e git+https://github.com/deepseek-ai/DeepEP@e3908bf5bd0cc6265bcb225d15cd8c996d4759ef#egg=deep_ep deep_gemm @ file:///tmp/tmp.timfv0OksY/deepgemm/dist/deep_gemm-2.0.0+ea9c5d9-cp312-cp312-linux_x86_64.whl depyf==0.20.0 dill==0.4.0 diskcache==5.6.3 distro==1.9.0 distro-info==1.1+ubuntu0.2 dnspython==2.8.0 docstring_parser==0.17.0 einops==0.8.1 email-validator==2.3.0 fastapi==0.125.0 fastapi-cli==0.0.11 fastapi-cloud-cli==0.1.5 fastrlock==0.8.3 filelock==3.19.1 flashinf...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: ==0.8.1 attrs==25.3.0 awscrt==0.27.6 bitsandbytes==0.47.0 blake3==1.0.5 blinker==1.4 boto3==1.40.30 botocore==1.40.30 build==1.3.0 cachetools==6.2.0 caio==0.9.24 cbor2==5.7.0 certifi==2025.8.3 cffi==2.0.0 charset-normal...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: vllm 0.12.0 fail to start Qwen3-VL-30B-A3B-Thinking bug ### Your current environment root@bfbeb5cfa732:/work# pip3 freeze accelerate==1.10.1 aiofile==3.9.0 aiofiles==24.1.0 aiohappyeyeballs==2.6.1 aiohttp==3.12.1...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: i-cli==0.0.11 fastapi-cloud-cli==0.1.5 fastrlock==0.8.3 filelock==3.19.1 flashinfer-python==0.5.3 frozendict==2.4.6 frozenlist==1.7.0 fsspec==2025.9.0 gguf==0.17.1 h11==0.16.0 hf-xet==1.1.10 hf_transfer==0.1.9 httpcore=...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ame" \ 49 --task generate \ 50 --load_format safetensors \ 51 --dtype bfloat16 \ 52 --max_model_len 16384 \ 53 --model_impl vllm \ 54 --media-io-kwargs '{"video": {"num_frames": -1}}' \ 55 --pipeline_parallel_size 1 \ 5...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ickle==3.1.1 cmake==4.1.0 compressed-tensors==0.12.2 cryptography==3.4.8 cuda-bindings==13.1.1 cuda-pathfinder==1.3.3 cuda-python==13.1.1 cufile-python==0.1.1 cupy-cuda12x==13.6.0 dbus-python==1.2.18 -e git+https://gith...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
