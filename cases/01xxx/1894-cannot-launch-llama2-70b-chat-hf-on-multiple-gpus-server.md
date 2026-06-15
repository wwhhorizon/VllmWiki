# vllm-project/vllm#1894: Cannot Launch llama2-70b-chat-hf on Multiple GPUs Server

| 字段 | 值 |
| --- | --- |
| Issue | [#1894](https://github.com/vllm-project/vllm/issues/1894) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Cannot Launch llama2-70b-chat-hf on Multiple GPUs Server

### Issue 正文摘录

Hi there, I am trying to launch an OpenAI server with dockerhub image on my server(4*A6000). ``` $ docker run --runtime nvidia --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ -p 1234:8000 \ --env "HUGGING_FACE_HUB_TOKEN=..." \ --shm-size=10.24gb vllm/vllm-openai \ --model meta-llama/Llama-2-70b-chat-hf \ --tensor-parallel-size 4 \ --tokenizer hf-internal-testing/llama-tokenizer ``` But the server only show it's initializing, for more than 15 minutes. I have reload for many times, and every time I interrupt the container, it shows same logs. ``` INFO 12-02 12:54:55 api_server.py:638] args: Namespace(host=None, port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name=None, model='meta-llama/Llama-2-70b-chat-hf', tokenizer='hf-internal-testing/llama-tokenizer', revision=None, tokenizer_revision=None, tokenizer_mode='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=4, block_size=16, seed=0, swap_space=4, gpu_memory_utilization=0.9, max_num_batched_tokens=None, max_num_seqs=256, max...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: Cannot Launch llama2-70b-chat-hf on Multiple GPUs Server Hi there, I am trying to launch an OpenAI server with dockerhub image on my server(4*A6000). ``` $ docker run --runtime nvidia --gpus all \ -v ~/.cache/huggingfac...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: tiple GPUs Server Hi there, I am trying to launch an OpenAI server with dockerhub image on my server(4*A6000). ``` $ docker run --runtime nvidia --gpus all \ -v ~/.cache/huggingface:/root/.cache/huggingface \ -p 1234:80...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: ='auto', trust_remote_code=False, download_dir=None, load_format='auto', dtype='auto', max_model_len=None, worker_use_ray=False, pipeline_parallel_size=1, tensor_parallel_size=4, block_size=16, seed=0, swap_space=4, gpu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: errupt ``` What should I do? Is there bug? And btw, here is my `nvidia-smi` log, when the container stuck. ``` $ nvidia-smi Sat Dec 2 20:53:45 2023 +----------------------------------------------------------------------...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: server.py:638] args: Namespace(host=None, port=8000, allow_credentials=False, allowed_origins=['*'], allowed_methods=['*'], allowed_headers=['*'], served_model_name=None, model='meta-llama/Llama-2-70b-chat-hf', tokenize...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
