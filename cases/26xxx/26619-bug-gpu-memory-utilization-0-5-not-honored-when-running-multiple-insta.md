# vllm-project/vllm#26619: [Bug]:--gpu-memory-utilization 0.5 Not Honored When Running Multiple Instances

| 字段 | 值 |
| --- | --- |
| Issue | [#26619](https://github.com/vllm-project/vllm/issues/26619) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;nan_inf;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]:--gpu-memory-utilization 0.5 Not Honored When Running Multiple Instances

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug docker-compose ``` services: embedding: # 组件名称【自行修改】 image: vllm/vllm-openai:v0.11.0 # 需要使用的镜像名【自行修改】 container_name: Qwen3-Embedding-0.6B # 建议与container_name一致【自行修改】 restart: always # 是否自动重启，建议always runtime: nvidia # 指定运行环境使用英伟达，容器内调用显卡的固定写法【无须修改】 ports: - "11435:8000" # 容器端口映射，前面是宿主机的端口，后面是容器内应用启动的端口，前面的宿主机端口可以【自行修改】 shm_size: '1g' # 共享内存设置，设置小了可能会导致模型无法启动，根据实际情况【自行修改】 volumes: - /home/install/modelscope/hub/Qwen/Qwen3-Embedding-0___6B:/data # 模型文件目录挂载，根据实际情况【自行修改】 environment: CUDA_VISIBLE_DEVICES: "1" # vllm支持通过该环境变量指定使用哪些显卡【自行修改】 HF_HUB_OFFLINE: 1 # vllm使用huggingface的模型时，指定离线模式【无须修改】 TZ: Asia/Shanghai # 设置容器时区为亚洲/上海【无须修改】 logging: # 日志配置，根据实际情况【自行修改】 driver: "json-file" options: max-size: "50m" max-file: "5" command: - --model #【无须修改】 - /data # 容器中的模型文件目录【无须修改】 - --served-model-name # 指定模型的key【无须修改】 - Qwen3-Embedding-0.6B # 模型启动后接口调用该模型传入的key【自行修改】 - --task # 指定模型的任务类型【无须修改】 - embed - --dtype # 模型的精度，一般在配置文件中有默认配置，bfloat16有些卡用不了，就使用float16 - float16 - --gpu-memory-utilization # 模型的GPU占用比例（如20G的显存设置0.9后，无论模型大小，固定占用20*0.9=18G的显存，最大为1，越靠近1性能越好），CUDA out of memory时可以适当降低【自行修改】 - "0.5" - --max_model_len # 指定模型的上下文长度【无须修改】 - "819...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: ances bug;stale ### Your current environment ### 🐛 Describe the bug docker-compose ``` services: embedding: # 组件名称【自行修改】 image: vllm/vllm-openai:v0.11.0 # 需要使用的镜像名【自行修改】 container_name: Qwen3-Embedding-0.6B # 建议与contain...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: image: vllm/vllm-openai:v0.11.0 # 需要使用的镜像名【自行修改】 container_name: Qwen3-Embedding-0.6B # 建议与container_name一致【自行修改】 restart: always # 是否自动重启，建议always runtime: nvidia # 指定运行环境使用英伟达，容器内调用显卡的固定写法【无须修改】 ports: - "11435:8000"...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: 模型传入的key【自行修改】 - --task # 指定模型的任务类型【无须修改】 - embed - --dtype # 模型的精度，一般在配置文件中有默认配置，bfloat16有些卡用不了，就使用float16 - float16 - --gpu-memory-utilization # 模型的GPU占用比例（如20G的显存设置0.9后，无论模型大小，固定占用20*0.9=18G的显存，最大为1，越靠近1性能越好），CUDA ou...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: 3-Embedding-0___6B:/data # 模型文件目录挂载，根据实际情况【自行修改】 environment: CUDA_VISIBLE_DEVICES: "1" # vllm支持通过该环境变量指定使用哪些显卡【自行修改】 HF_HUB_OFFLINE: 1 # vllm使用huggingface的模型时，指定离线模式【无须修改】 TZ: Asia/Shanghai # 设置容器时区为亚洲/上海【无须修改】 logging...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: u-memory-utilization 0.5 Not Honored When Running Multiple Instances bug;stale ### Your current environment ### 🐛 Describe the bug docker-compose ``` services: embedding: # 组件名称【自行修改】 image: vllm/vllm-openai:v0.11.0 # 需...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
