# vllm-project/vllm#32575: [Bug]: MinerU fails to start on DGX Spark using docker images vllm/vllm-openai:nightly-aarch64

| 字段 | 值 |
| --- | --- |
| Issue | [#32575](https://github.com/vllm-project/vllm/issues/32575) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;multimodal_vlm;quantization;scheduler_memory |
| 子分类 | cold_start |
| Operator 关键词 | attention;cache;cuda;kernel;operator;quantization;triton |
| 症状 | build_error;crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: MinerU fails to start on DGX Spark using docker images vllm/vllm-openai:nightly-aarch64

### Issue 正文摘录

### Your current environment **Dockerfile** : `# Use DaoCloud mirrored vllm image for China region for gpu with Volta、Turing、Blackwell architecture (7.0 = 10.0) # support x86_64 architecture and ARM(AArch64) architecture FROM docker.m.daocloud.io/vllm/vllm-openai:nightly-aarch64 #FROM nvcr.io/nvidia/vllm:25.12.post1-py3 # Install libgl for opencv support & Noto fonts for Chinese characters RUN apt-get update && \ apt-get install -y \ fonts-noto-core \ fonts-noto-cjk \ fontconfig \ libgl1 && \ fc-cache -fv && \ apt-get clean && \ rm -rf /var/lib/apt/lists/* # Install mineru latest RUN python3 -m pip install -U 'mineru[vlm,pipeline,api]>=2.7.0' -i https://mirrors.aliyun.com/pypi/simple --break-system-packages && \ python3 -m pip cache purge # Download models and update the configuration file RUN /bin/bash -c "mineru-models-download -s modelscope -m all" # Set the entry point to activate the virtual environment and run the command line tool ENTRYPOINT ["/bin/bash", "-c", "export MINERU_MODEL_SOURCE=local && exec \"$@\"", "--"]` **compose.yaml** `services: mineru-vllm-server: image: mineru-vllm:latest container_name: mineru-vllm-server restart: always profiles: ["vllm-server"] ports:...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: MinerU fails to start on DGX Spark using docker images vllm/vllm-openai:nightly-aarch64 bug ### Your current environment **Dockerfile** : `# Use DaoCloud mirrored vllm image for China region for gpu with Volta、Tu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ails to start on DGX Spark using docker images vllm/vllm-openai:nightly-aarch64 bug ### Your current environment **Dockerfile** : `# Use DaoCloud mirrored vllm image for China region for gpu with Volta、Turing、Blackwell...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: tall -y \ fonts-noto-core \ fonts-noto-cjk \ fontconfig \ libgl1 && \ fc-cache -fv && \ apt-get clean && \ rm -rf /var/lib/apt/lists/* # Install mineru latest RUN python3 -m pip install -U 'mineru[vlm,pipeline,api]>=2.7...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 5: apt-get clean && \ rm -rf /var/lib/apt/lists/* # Install mineru latest RUN python3 -m pip install -U 'mineru[vlm,pipeline,api]>=2.7.0' -i https://mirrors.aliyun.com/pypi/simple --break-system-packages && \ python3 -m pi...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 4: ) - (12.0) warnings.warn( 2026-01-18 23:16:55.275 | INFO | mineru.backend.vlm.utils:enable_custom_logits_processors:46 - compute_capability: 12.1 >= 8.0 and vllm version: 0.14.0rc1.dev539+g11b6af528 >= 0.10.1, enable cu...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
