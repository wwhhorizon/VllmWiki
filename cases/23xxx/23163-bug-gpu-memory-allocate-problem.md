# vllm-project/vllm#23163: [Bug]: GPU memory allocate problem

| 字段 | 值 |
| --- | --- |
| Issue | [#23163](https://github.com/vllm-project/vllm/issues/23163) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: GPU memory allocate problem

### Issue 正文摘录

### Your current environment dockerfile: ``` FROM vllm/vllm-openai:latest RUN apt-get update && \ apt-get install -y \ locales \ apache2-utils \ cron &&\ rm -rf /var/lib/apt/lists/* && \ locale-gen zh_CN.UTF-8 && \ update-locale LANG=zh_CN.UTF-8 RUN locale-gen zh_CN.UTF-8 && \ update-locale LANG=zh_CN.UTF-8 ENV LANG zh_CN.UTF-8 ENV LANGUAGE zh_CN:zh ENV LC_ALL zh_CN.UTF-8 RUN mkdir -p /app COPY spark-tts-server /app/spark-tts-server WORKDIR /app/spark-tts-server ENTRYPOINT [] ``` model: ``` modelscope download --model SparkAudio/Spark-TTS-0.5B --local_dir ./Spark-TTS-0___5B mv Spark-TTS-0___5B/LLM sparkttsllm ``` launch: ``` docker run --restart=always --gpus all -itd \ -v /data1/logs/vllm/30001:/logs \ -e VLLM_USE_V1=1 \ --shm-size "100g" --memory "100g" \ --net host \ --name "clone_vllm_30001_0.1" \ 0693a8ee9ab5 \ bash -c "export VLLM_LOGGING_LEVEL=DEBUG && \ vllm serve sparkttsllm \ --gpu-memory-utilization 0.1 \ --enable-chunked-prefill \ --max-model-len 3000 \ --swap-space 20 \ --block-size 32 \ --dtype bfloat16 \ --port 30001 | \ rotatelogs -l /logs/vllm_server.%Y-%m-%d-%H.log 3600" ``` ### 🐛 Describe the bug Using the above configuration, I created three instances on the L2...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: \ --swap-space 20 \ --block-size 32 \ --dtype bfloat16 \ --port 30001 | \ rotatelogs -l /logs/vllm_server.%Y-%m-%d-%H.log 3600" ``` ### 🐛 Describe the bug Using the above configuration, I created three instances on the...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ug]: GPU memory allocate problem bug;stale ### Your current environment dockerfile: ``` FROM vllm/vllm-openai:latest RUN apt-get update && \ apt-get install -y \ locales \ apache2-utils \ cron &&\ rm -rf /var/lib/apt/li...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 01, 30002, and 30003 respectively. After stress testing, why does nvidia-smi show that the occupied memory is 6598MiB, 7904MiB, and 12570MiB respectively? why not same? ### Before submitting a new issue... - [x] Make su...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: er /app/spark-tts-server WORKDIR /app/spark-tts-server ENTRYPOINT [] ``` model: ``` modelscope download --model SparkAudio/Spark-TTS-0.5B --local_dir ./Spark-TTS-0___5B mv Spark-TTS-0___5B/LLM sparkttsllm ``` launch: ``...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: [Bug]: GPU memory allocate problem bug;stale ### Your current environment dockerfile: ``` FROM vllm/vllm-openai:latest RUN apt-get update && \ apt-get install -y \ locales \ apache2-utils \ cron &&\ rm -rf /var/lib/apt/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
