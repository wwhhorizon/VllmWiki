# vllm-project/vllm#20310: [Bug]: can't run dp just in 2 gpus

| 字段 | 值 |
| --- | --- |
| Issue | [#20310](https://github.com/vllm-project/vllm/issues/20310) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: can't run dp just in 2 gpus

### Issue 正文摘录

### Your current environment pip list Package Version ---------------------------------------- ----------------------------- absl-py 2.1.0 accelerate 1.4.0 aenum 3.1.15 aiohappyeyeballs 2.4.6 aiohttp 3.11.12 aiohttp-cors 0.7.0 aiosignal 1.3.2 airportsdata 20241001 annotated-types 0.7.0 antlr4-python3-runtime 4.13.2 anyio 4.8.0 astor 0.8.1 asttokens 3.0.0 async-timeout 5.0.1 attrs 25.1.0 beautifulsoup4 4.13.3 bitsandbytes 0.45.2 blake3 1.0.4 blis 0.7.11 cachetools 5.5.1 catalogue 2.0.10 certifi 2025.1.31 chardet 5.2.0 charset-normalizer 3.4.1 click 8.1.8 cloudpathlib 0.16.0 cloudpickle 3.1.1 colorama 0.4.6 coloredlogs 15.0.1 colorful 0.5.6 colorlog 6.9.0 comm 0.2.2 compressed-tensors 0.10.2 confection 0.1.5 contourpy 1.3.1 cos-python-sdk-v5 1.9.25 coscmd 1.8.6.30 crcmod 1.7 cupy-cuda12x 13.4.1 cycler 0.12.1 cymem 2.0.11 DataProperty 1.1.0 datasets 3.3.1 DateTime 5.5 debugpy 1.8.12 decorator 5.1.1 deepspeed 0.15.4 depyf 0.18.0 dill 0.3.8 diskcache 5.6.3 distilabel 1.5.3 distlib 0.3.9 distro 1.9.0 dnspython 2.7.0 docker-pycreds 0.4.0 dulwich 0.22.7 einops 0.8.1 email_validator 2.2.0 executing 2.2.0 fastapi 0.115.8 fastapi-cli 0.0.7 fastrlock 0.8.3 filelock 3.17.0 flake8 7.1.2 flatbuf...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 9: r current environment pip list Package Version ---------------------------------------- ----------------------------- absl-py 2.1.0 accelerate 1.4.0 aenum 3.1.15
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 7: [Bug]: can't run dp just in 2 gpus bug;stale ### Your current environment pip list Package Version ---------------------------------------- ----------------------------- absl-py 2.1.0 accelera
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: 1.70.0 h11 0.14.0 hf_transfer 0.1.9 hf-xet 1.1.5 hjson 3.1.0 httpcore 1.0.7 httptools
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ride_neuron_config={}, tokenizer_revision=None, trust_remote_code=False, dtype=torch.bfloat16, max_seq_len=131072, download_dir=None, load_format=LoadFormat.AUTO, tensor_parallel_size=1, pipeline_parallel_size=1, disabl...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: 5.14.3 transformers 4.53.0 triton 3.3.0 trl 0.16.0.dev0 typepy 1.3.4 typer 0.16.0 typing_extensions

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
