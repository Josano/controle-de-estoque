<script>
import { 
	Button, 
	Container, 
	Jumbotron, 
	Row, 
	Card, 
	CardBody, 
	CardFooter, 
	Col,
	Input,
	InputGroup,
	Badge
} from 'sveltestrap';

let title = "";

let products = [
	{
		id: 1,
		status: true,
		title: 'Procesador Ryzen 5 2400G 3.4MHZ 12MB 8 Threads'
	},
	{
		id: 2,
		status: false,
		title: 'Placa mãe AORUS Gigabyte B450M, 7 USB 3.0'
	},
	{
		id: 3,
		status: true,
		title: '3 Fan Corsair RGB mais controladora'
	}		
];

function addProduct(ev) {
	ev.preventDefault();
	const product = { id: 4, title: title, status: true };
	products = [...products, product];
	clearField();
}

function clearField(){
	title = "";
}

function stock(p) {
	p.status = p.status ? false : true;
	products[products.indexOf(p)] = p;
}
</script>

<style>
	.cardDisabled {
		opacity: 0.6;
	}
</style>

<Container class="mt-5">
	<h4 class="text-center text-muted">Controle de Estoque</h4>
</Container>

<Jumbotron>
	<Container>
		<Row>
			<Col sm="12" class="mb-3">
				<h5 class="text-muted">Em estoque 
					<Badge color="primary">{ products.length }</Badge>
				</h5>
			</Col>
		{#each products as product}			
			<Col sm="12" lg="4" class="mb-3">
				<card class="card h-100 {product.status == false ? 'cardDisabled' : ''}">
					<CardBody>{product.title}</CardBody>
					<CardFooter class="text-right">
						<Button 
						 color="success"
						 disabled={product.status}
						 on:click={() => stock(product)}>
							<i class="fas fa-sync" />
						</Button>
						<Button color="info" disabled={!product.status} on:click={() => stock(product)}>
							<i class="fas fa-folder-open" />
						</Button>						
					</CardFooter>
				</card>
			</Col>						
		{/each}			
		</Row>
	</Container>
</Jumbotron>

<Container>
	<form>
		<InputGroup>
			<Col>
				<Input placeholder="Insira um título" bind:value={title} autofocus/>
			</Col>
		</InputGroup>
		<InputGroup class="text-right mt-3">
			<Col>
				<Button disabled={!title} color="success" on:click={addProduct}>Adicionar</Button>
			</Col>
		</InputGroup>		
	</form>
</Container>