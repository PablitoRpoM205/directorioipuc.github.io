const departments = [
  { name: "Amazonas", src: "https://www.google.com/maps/d/u/0/embed?mid=1MdmNiX7U1LJEpfmpsWDKd82QKP6OhM4&ehbc=2E312F" },
  { name: "Antioquia", src: "https://www.google.com/maps/d/u/0/embed?mid=1Q_QVn5PpkvyjtjLBJFzldPKXO1SexMc&ehbc=2E312F" },
  { name: "Arauca", src: "https://www.google.com/maps/d/u/0/embed?mid=1K5BmrZOXABGnn6biyfOMerYW6gG5nRo&ehbc=2E312F" },
  { name: "Atlántico", src: "https://www.google.com/maps/d/u/0/embed?mid=1ptihJv7Y3h-wI1PzO2rLv2CWfsfabCY&ehbc=2E312F" },
  { name: "Bogotá D.C.", src: "https://www.google.com/maps/d/u/0/embed?mid=1Wr7Dwyrrgm37D0XnlbAW5CVvReV98h0&ehbc=2E312F" },
  { name: "Bolívar", src: "https://www.google.com/maps/d/u/0/embed?mid=1iit_8qJ7ZBJI7WRdYXMPjNvgqHcnld8&ehbc=2E312F" },
  { name: "Boyacá", src: "https://www.google.com/maps/d/u/0/embed?mid=1ILCaR4_D9vq1-9eiRbZ2ACbiB9o7KbU&ehbc=2E312F" },
  { name: "Caldas", src: "https://www.google.com/maps/d/u/0/embed?mid=10w38FTCCbnIZKBSTEEjQuJ1jrznz1Rs&ehbc=2E312F" },
  { name: "Caquetá", src: "https://www.google.com/maps/d/u/0/embed?mid=1Eq8A4efusHz-dWf0z8XI75RX09ln16o&ehbc=2E312F" },
  { name: "Casanare", src: "https://www.google.com/maps/d/u/0/embed?mid=1vWtF6i5Pn6LGAE_sDMBlCmrCLhSKP4E&ehbc=2E312F" },
  { name: "Cauca", src: "https://www.google.com/maps/d/u/0/embed?mid=12-WoKRN2tByshGrKax1Mi8u8e6vzIq8&ehbc=2E312F" },
  { name: "Cesar", src: "https://www.google.com/maps/d/u/0/embed?mid=15cDnIOxq4eoDiotK-lP1vurTtJQ_rl8&ehbc=2E312F" },
  { name: "Chocó", src: "https://www.google.com/maps/d/u/0/embed?mid=1g6mTAVhPi1BqAX_M3I3DRoC8AlHcLcI&ehbc=2E312F" },
  { name: "Córdoba", src: "https://www.google.com/maps/d/u/0/embed?mid=1d8B1CVXuNhXcAHMfjCoECl7HN5ssTtk&ehbc=2E312F" },
  { name: "Cundinamarca", src: "https://www.google.com/maps/d/u/0/embed?mid=1zm24OaRc_y6EhPr7v1ENRn4hK-SEwgc&ehbc=2E312F" },
  { name: "Guainía", src: "https://www.google.com/maps/d/u/0/embed?mid=1vqbXYDkzuLNoA9V5-YVfpOe9Rfpb0o0&ehbc=2E312F" },
  { name: "Guaviare", src: "https://www.google.com/maps/d/u/0/embed?mid=1ht8nand8N-E7UjI870NvXmrJ1Q7GvAs&ehbc=2E312F" },
  { name: "Huila", src: "https://www.google.com/maps/d/u/0/embed?mid=1S1d-v_pYO7cLIUF7gMmLwcOAkP4iFSI&ehbc=2E312F" },
  { name: "La Guajira", src: "https://www.google.com/maps/d/u/0/embed?mid=1ZIOw6p-Nc1eBdHEtG6iDAzgJfyyAjzY&ehbc=2E312F" },
  { name: "Magdalena", src: "https://www.google.com/maps/d/u/0/embed?mid=14SN52R8sH7GXNXOgA2l77vifX6wiS64&ehbc=2E312F" },
  { name: "Meta", src: "https://www.google.com/maps/d/u/0/embed?mid=1OuSItI8FQ7eqfalRSSLne0gLY--78e0&ehbc=2E312F" },
  { name: "Nariño", src: "https://www.google.com/maps/d/u/0/embed?mid=1QA7Csg6x_kq6uSVshcpUQ1sWzYyzcuM&ehbc=2E312F" },
  { name: "Norte de Santander", src: "https://www.google.com/maps/d/u/0/embed?mid=1gHqm46hitwTafFgqujahRIjP6e5Wpo4&ehbc=2E312F" },
  { name: "Putumayo", src: "https://www.google.com/maps/d/u/0/embed?mid=1Upec4bkkaBhv71rbMm_eT4hFOAtRjSU&ehbc=2E312F" },
  { name: "Quindío", src: "https://www.google.com/maps/d/u/0/embed?mid=1pZqCR6T-DC_sqAVmjeL7TfIGMS5uvBk&ehbc=2E312F" },
  { name: "Risaralda", src: "https://www.google.com/maps/d/u/0/embed?mid=1qcEWxSmPaQOvtuqqaAsWeR2CBJHS0es&ehbc=2E312F" },
  { name: "San Andrés y Providencia", src: "https://www.google.com/maps/d/u/0/embed?mid=1z2OJ3IizUcyLw55vRdaR3Dr-jdNiutw&ehbc=2E312F" },
  { name: "Santander", src: "https://www.google.com/maps/d/u/0/embed?mid=1AF5FvDAnkAPs5pKo1e-G8SAuGlXfgUw&ehbc=2E312F" },
  { name: "Sedes distritales, CAN y fundaciones", src: "https://www.google.com/maps/d/u/0/embed?mid=1JqNgEpeu21slg-qtLKkZ9Iy7Q06qTls&ehbc=2E312F", isHQ: true },
  { name: "Sucre", src: "https://www.google.com/maps/d/u/0/embed?mid=1Sb7atk57nP3QI3SyvEyR_LuwMye6-d4&ehbc=2E312F" },
  { name: "Tolima", src: "https://www.google.com/maps/d/u/0/embed?mid=1IY2lRb6CA8i1IYuE-9pKohgUzRBspHU&ehbc=2E312F" },
  { name: "Valle del Cauca", src: "https://www.google.com/maps/d/u/0/embed?mid=1NsE4S1wnuIpbQMHOSc7AjqDOaEtMieA&ehbc=2E312F" },
  { name: "Vaupés", src: "https://www.google.com/maps/d/u/0/embed?mid=1pDACZRKYFwaBILafnnAdGnTV0HzpSfE&ehbc=2E312F" },
  { name: "Vichada", src: "https://www.google.com/maps/d/u/0/embed?mid=17aLuNb-8UJT33Y3wlvcOS8mUuvgtjNE&ehbc=2E312F" }
];

const listElement = document.getElementById("departmentList");
const mapFrame = document.getElementById("mapFrame");
const mapTitle = document.getElementById("mapTitle");
const mapDescription = document.getElementById("mapDescription");
const searchInput = document.getElementById("search");
const toggleButton = document.getElementById("toggleSidebar");
const sidebar = document.getElementById("sidebar");
const totalCountElement = document.getElementById("totalCount");
let activeIndex = 0;
let counts = {};

function createDepartmentItem(department, index) {
  const item = document.createElement("button");
  item.type = "button";
  item.className = "department-item";
  const countText = department.count != null ? `${department.count}` : "N/D";
  item.innerHTML = `<span>${department.name}</span><span class="department-count">${countText}</span>`;
  item.dataset.index = index;
  item.addEventListener("click", () => {
    setActiveDepartment(index);
    closeSidebarOnMobile();
  });
  return item;
}

function renderDepartmentList(filter = "") {
  const query = filter.trim().toLowerCase();
  listElement.innerHTML = "";

  departments.forEach((department, index) => {
    if (!query || department.name.toLowerCase().includes(query)) {
      const item = createDepartmentItem(department, index);
      if (index === activeIndex) item.classList.add("active");
      listElement.appendChild(item);
    }
  });
}

function setActiveDepartment(index) {
  activeIndex = index;
  const department = departments[index];
  mapFrame.src = department.src;
  mapTitle.textContent = department.name;
  
  // Excepción para "Sedes distritales, CAN y fundaciones"
  if (department.isHQ) {
    mapDescription.textContent = `Centro Administrativo Nacional, sedes distritales y fundaciones de la IPUC.`;
  } else {
    mapDescription.textContent = `Mapa de congregaciones de la IPUC en ${department.name}.`;
  }
  
  updateActiveButton();
}

async function loadDepartmentCounts() {
  try {
    const response = await fetch('department-counts.json');
    if (!response.ok) throw new Error('No se pudo cargar los conteos');
    
    const data = await response.json();
    counts = data.departments || {};
    
    // Actualizar datos de departamentos con conteos
    departments.forEach(dept => {
      if (counts[dept.name] !== undefined && counts[dept.name] !== null) {
        dept.count = counts[dept.name];
      }
    });
    
    // Mostrar total de congregaciones
    if (data.total && totalCountElement) {
      totalCountElement.textContent = data.total.toLocaleString('es-CO');
    }
    
    // Re-renderizar lista para mostrar conteos
    renderDepartmentList();
  } catch (error) {
    console.log('Conteos no disponibles (usa department-counts-example.json como referencia)');
  }
}

function updateActiveButton() {
  Array.from(listElement.children).forEach((button) => {
    const buttonIndex = Number(button.dataset.index);
    button.classList.toggle("active", buttonIndex === activeIndex);
  });
}

function closeSidebarOnMobile() {
  if (window.innerWidth <= 860) {
    sidebar.classList.remove("open");
  }
}

searchInput.addEventListener("input", (event) => {
  renderDepartmentList(event.target.value);
  updateActiveButton();
});

toggleButton.addEventListener("click", () => {
  sidebar.classList.toggle("open");
});

window.addEventListener("resize", () => {
  if (window.innerWidth > 860) {
    sidebar.classList.remove("open");
  }
});

renderDepartmentList();
loadDepartmentCounts().then(() => {
  setActiveDepartment(0);
}).catch(() => {
  setActiveDepartment(0);
});
