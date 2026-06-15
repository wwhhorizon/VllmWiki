# vllm-project/vllm#3226: vllm load SqueezeLLM quantization model failed

| 字段 | 值 |
| --- | --- |
| Issue | [#3226](https://github.com/vllm-project/vllm/issues/3226) |
| 状态 | closed |
| 标签 | stale |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> vllm load SqueezeLLM quantization model failed

### Issue 正文摘录

### This is my env version: ``` torch:2.2.1 transformers: 4.39.0.dev0 vllm: custom compile at master@24aecf421a4ad5989697010963074904fead9a1b ``` ### I use SqueezeLLM quantization my llama-7B trained model and want use vllm load, below is my code and traceback ``` #git clone https://github.com/SqueezeAILab/SqueezeLLM.git #git clone https://github.com/kssteven418/SqueezeLLM-gradients.git #conda create -n sqllm-grad python=3.9 -y #conda activate sqllm-grad #cd SqueezeLLM-gradients #pip install -e . #pip install -r requirements.txt(mod torch>=2.2.1) ### Compute gradients CUDA_DEVICE_ORDER=PCI_BUS_ID CUDA_VISIBLE_DEVICES=16 python run.py --output_dir [gradients_path] --model_name_or_path [model_path] #cd SqueezeLLM/ #pip install -e . #cd squeezellm python setup_cuda.py install #cd ../quantization ### Chunk model weights and gradients python chunk_models.py --model [model_path] --output [model_chunk_path] --model_type llama python chunk_models.py --model [gradients_path] --output [gradients_chunk_path] --model_type llama ### (Optional for D+S quantization) Outlier configuration generation python generate_outlier_config.py --model [model_chunk_path] --range 1.8 --output [outlier_config]...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: vllm load SqueezeLLM quantization model failed stale ### This is my env version: ``` torch:2.2.1 transformers: 4.39.0.dev0 vllm: custom compile at master@24aecf421a4ad5989697010963074904fead9a1b ``` ### I use SqueezeLLM...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: vllm load SqueezeLLM quantization model failed stale ### This is my env version: ``` torch:2.2.1 transformers: 4.39.0.dev0 vllm: custom compile at master@24aecf421a4ad5989697010963074904fead9a1b ``` ### I use SqueezeLLM...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: vllm load SqueezeLLM quantization model failed stale ### This is my env version: ``` torch:2.2.1 transformers: 4.39.0.dev0 vllm: custom compile at master@24aecf421a4ad5989697010963074904fead9a1b ``` ### I use SqueezeLLM...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: salLM.from_config(config, torch_dtype=torch.bfloat16) model = model.eval() layers = find_layers(model) state_dict = torch.load(os.path.join(checkpoint, "pack_model.pt")) # load sparse thresholds from checkpoint if inclu...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: #pip install -r requirements.txt(mod torch>=2.2.1) ### Compute gradients CUDA_DEVICE_ORDER=PCI_BUS_ID CUDA_VISIBLE_DEVICES=16 python run.py --output_dir [gradients_path] --model_name_or_path [model_path] #cd SqueezeLLM/...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
