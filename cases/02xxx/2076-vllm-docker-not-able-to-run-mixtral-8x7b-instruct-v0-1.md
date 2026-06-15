# vllm-project/vllm#2076: Vllm Docker not able to run Mixtral-8x7B-Instruct-v0.1

| 字段 | 值 |
| --- | --- |
| Issue | [#2076](https://github.com/vllm-project/vllm/issues/2076) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support |
| 子分类 |  |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Vllm Docker not able to run Mixtral-8x7B-Instruct-v0.1

### Issue 正文摘录

Hi, I am trying to run Mixtral-8x7B-Instruct-v0.1 model using the docker Image. docker run --gpus all \ -e HF_TOKEN="" -p 8000:8000 \ ghcr.io/mistralai/mistral-src/vllm:latest \ --host 0.0.0.0 \ --model mistralai/Mixtral-8x7B-Instruct-v0.1 \ --tensor-parallel-size 4 \ --load-format pt \ --dtype half The error i am getting when i run the above docker image: ValueError: Model architectures ['MixtralForCausalLM'] are not supported for now. Supported architectures: ['AquilaModel', 'BaiChuanForCausalLM', 'BaichuanForCausalLM', 'BloomForCausalLM', 'FalconForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'InternLMForCausalLM', 'LlamaForCausalLM', 'LLaMAForCausalLM', 'MistralForCausalLM', 'MPTForCausalLM', 'OPTForCausalLM', 'QWenLMHeadModel', 'RWForCausalLM'] I am using p3.8xlarge instance to run the model. This is my spec: +---------------------------------------------------------------------------------------+ | NVIDIA-SMI 535.54.03 Driver Version: 535.54.03 CUDA Version: 12.2 | |-----------------------------------------+----------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: Vllm Docker not able to run Mixtral-8x7B-Instruct-v0.1 Hi, I am trying to run Mixtral-8x7B-Instruct-v0.1 model using the docker Image. docker run --gpus all \ -e HF_TOKEN="" -p 8000:8000 \ ghcr.io/mistralai/mistral-s
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: al-8x7B-Instruct-v0.1 Hi, I am trying to run Mixtral-8x7B-Instruct-v0.1 model using the docker Image. docker run --gpus all \ -e HF_TOKEN="" -p 8000:8000 \ ghcr.io/mistralai/mistral-src/vllm:latest \ --host 0.0.0.0 \ --...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: am getting when i run the above docker image: ValueError: Model architectures ['MixtralForCausalLM'] are not supported for now. Supported architectures: ['AquilaModel', 'BaiChuanForCausalLM', 'BaichuanForCausalLM', 'Blo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: truct-v0.1 \ --tensor-parallel-size 4 \ --load-format pt \ --dtype half The error i am getting when i run the above docker image: ValueError: Model architectures ['MixtralForCausalLM'] are not supported for now. Support...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: ctures: ['AquilaModel', 'BaiChuanForCausalLM', 'BaichuanForCausalLM', 'BloomForCausalLM', 'FalconForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'InternLMForCausalLM',...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
