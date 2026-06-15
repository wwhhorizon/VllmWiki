# vllm-project/vllm#14178: [Bug]: Failed to run example.py even if the pytorch framework has been compiled natively.

| 字段 | 值 |
| --- | --- |
| Issue | [#14178](https://github.com/vllm-project/vllm/issues/14178) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;quantization |
| 子分类 | install |
| Operator 关键词 | attention;cuda;kernel;operator;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Failed to run example.py even if the pytorch framework has been compiled natively.

### Issue 正文摘录

### Your current environment Greetings, everyone. 1. I have build the Pytorch 2.5.1 from scratch on the Jetson AGX orin with CUDA support. So I have got following output from CLI: Python 3.10.16 (main, Dec 11 2024, 16:18:56) [GCC 11.2.0] on linux Type "help", "copyright", "credits" or "license" for more information. import torch print(torch.version.cuda) 12.6 print(torch.cuda.get_arch_list()) **['sm_87']** As you can see, it should support the sm_87 capability. 2. And yes, I have followed these setup to build the lasted vllm code from github. $ python use_existing_torch.py $ pip install -r requirements-build.txt $ pip install -vvv -e . --no-build-isolation 3. What is more, I edited this file: /home/nvidia/projects/vllm/.deps/flashmla-src/setup.py And change the line from: cc_flag.append("arch=compute_90a,code=sm_90a") to cc_flag.append("arch=compute_87,code=sm_87") # for jetson agx orin 4. Everything can be compiled and then I try to run: CUDA_LAUNCH_BLOCKING=1 python examples/offline_inference/basic/basic.py I got following errors: INFO 03-04 11:23:24 [config.py:576] This model supports multiple tasks: {'embed', 'generate', 'score', 'classify', 'reward'}. Defaulting to 'generate'...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: [Bug]: Failed to run example.py even if the pytorch framework has been compiled natively. bug ### Your current environment Greetings, everyone. 1. I have build the Pytorch 2.5.1 from scratch on the Jetson AGX orin with...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: I have build the Pytorch 2.5.1 from scratch on the Jetson AGX orin with CUDA support. So I have got following output from CLI: Python 3.10.16 (main, Dec 11 2024, 16:18:56) [GCC 11.2.0] on linux Type "help", "copyright",...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: .7.4.dev180+gb87c21fc.d20250304) with config: model='facebook/opt-125m', speculative_config=None, tokenizer='facebook/opt-125m', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, override_neuron_config=None...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: de_neuron_config=None, tokenizer_revision=None, trust_remote_code=False, dtype=torch.float16, max_seq_len=2048, download_dir=None, load_format=auto, tensor_parallel_size=1, pipeline_parallel_size=1, disable_custom_all_r...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: gx orin 4. Everything can be compiled and then I try to run: CUDA_LAUNCH_BLOCKING=1 python examples/offline_inference/basic/basic.py I got following errors: INFO 03-04 11:23:24 [config.py:576] This model supports multip...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
