# vllm-project/vllm#6955: [Performance]: In tokens processing performance. Bad scaling with tensor-parallel

| 字段 | 值 |
| --- | --- |
| Issue | [#6955](https://github.com/vllm-project/vllm/issues/6955) |
| 状态 | closed |
| 标签 | performance;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | throughput |
| Operator 关键词 | cache;quantization |
| 症状 |  |
| 根因提示 | dtype |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Performance]: In tokens processing performance. Bad scaling with tensor-parallel

### Issue 正文摘录

### Proposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) I run vllm in docker with tensor-parallel. llama 3 70b family. Here is example of docker command: `sudo docker run --shm-size=32g --log-opt max-size=10m --log-opt max-file=1 --rm -it --gpus '"device=0,1,2,3"' -p 9000:8000 --mount type=bind,source=/home/me/.cache,target=/root/.cache vllm/vllm-openai:v0.5.3.post1 --model hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --tensor-parallel-size 4 --dtype half` I have lot of tests with parallel load. There is no problems with kv cache size. I test it with tensor-parallel 2 and 4. OUT tokens generation speed increased with tensor-parallel: 1 client. 30tps -> 46tps 5 clients. 121tps -> 152tps IN token processing performance is almost the same(little degraded): 1 client. 361tps -> 386 tps 5 clients. 525tps -> 490tps The same values i see in docker log. Is it possible to optimize IN token processing? May be some parallel execution? I test it on my server: epyc 7002(48 cores), 64gb ram, 4x3090ti(connected 16x pcie 4.0), ssd disk. Ub...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: # Your current environment (if you think it is necessary) I run vllm in docker with tensor-parallel. llama 3 70b family. Here is example of docker command: `sudo docker run --shm-size=32g --log-opt max-size=10m --log-op...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: .cache,target=/root/.cache vllm/vllm-openai:v0.5.3.post1 --model hugging-quants/Meta-Llama-3.1-70B-Instruct-AWQ-INT4 --tensor-parallel-size 4 --dtype half` I have lot of tests with parallel load. There is no problems wi...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: f you think it is necessary) I run vllm in docker with tensor-parallel. llama 3 70b family. Here is example of docker command: `sudo docker run --shm-size=32g --log-opt max-size=10m --log-opt max-file=1 --rm -it --gpus...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: roposal to improve performance _No response_ ### Report of performance regression _No response_ ### Misc discussion on performance _No response_ ### Your current environment (if you think it is necessary) I run vllm in...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: half` I have lot of tests with parallel load. There is no problems with kv cache size. I test it with tensor-parallel 2 and 4. OUT tokens generation speed increased with tensor-parallel: 1 client. 30tps -> 46tps 5 clien...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
